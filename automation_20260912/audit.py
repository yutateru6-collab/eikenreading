import argparse
import json
import re
from collections import Counter
from pathlib import Path

from data import SETS

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "automation-20260912"
OUT.mkdir(parents=True, exist_ok=True)


def wc(text):
    return len(re.findall(r"\b[A-Za-z]+(?:['’-][A-Za-z]+)*\b", text))


def all_questions(s):
    q = list(s['part1'])
    q += s['part2a']['questions'] + s['part2b']['questions']
    q += s['part3a']['questions'] + s['part3b']['questions']
    return sorted(q, key=lambda x: x['num'])


def check_content():
    report = {}
    failures = []
    for s in SETS:
        slug = s['slug']
        qs = all_questions(s)
        nums = [x['num'] for x in qs]
        answers = [x['answer'] for x in qs]
        counts = Counter(answers)
        r = {
            'questions': len(qs),
            'answer_counts': dict(sorted(counts.items())),
            'answer_sequence': answers,
            'word_counts': {
                'part2a': sum(wc(x) for x in s['part2a']['paragraphs']),
                'part2b': sum(wc(x) for x in s['part2b']['paragraphs']),
                'part3a': sum(wc(x) for x in s['part3a']['paragraphs']),
                'part3b': sum(wc(x) for x in s['part3b']['paragraphs']),
            },
        }
        report[slug] = r
        if nums != list(range(1, 32)):
            failures.append(f"{slug}: question numbers are not exactly 1-31: {nums}")
        if len(qs) != 31:
            failures.append(f"{slug}: expected 31 questions, got {len(qs)}")
        if sorted(counts.values()) != [7, 8, 8, 8]:
            failures.append(f"{slug}: answer distribution must be 8/8/8/7, got {dict(counts)}")
        for i in range(len(answers)-2):
            if answers[i] == answers[i+1] == answers[i+2]:
                failures.append(f"{slug}: three identical answer positions in a row at Q{i+1}-{i+3}")
        for x in qs:
            if len(x['choices']) != 4:
                failures.append(f"{slug} Q{x['num']}: choices != 4")
            if x['answer'] not in (1,2,3,4):
                failures.append(f"{slug} Q{x['num']}: invalid answer")
            if len(set(x['choices'])) != 4:
                failures.append(f"{slug} Q{x['num']}: duplicate choices")
            if not x.get('explanation','').strip():
                failures.append(f"{slug} Q{x['num']}: missing explanation")
        w = r['word_counts']
        for key in ('part2a','part2b'):
            if not (230 <= w[key] <= 275):
                failures.append(f"{slug}: {key} expected near 240-260 words; got {w[key]}")
        if not (190 <= w['part3a'] <= 250):
            failures.append(f"{slug}: part3a expected near 200-240 words; got {w['part3a']}")
        if not (330 <= w['part3b'] <= 390):
            failures.append(f"{slug}: part3b expected near 350-370 words; got {w['part3b']}")
        for key, n in [('part2a',3),('part2b',3),('part3a',3),('part3b',4)]:
            if len(s[key].get('translation',[])) != n:
                failures.append(f"{slug}: {key} translation paragraph count mismatch")
            if any(not x.strip() for x in s[key].get('translation',[])):
                failures.append(f"{slug}: {key} has blank translation paragraph")
    (OUT/'content_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    if failures:
        print("CONTENT AUDIT FAILURES:")
        for x in failures: print("-",x)
        raise SystemExit(1)


def check_pdfs():
    import fitz
    failures=[]
    report={}
    a4w,a4h=595.28,841.89
    for s in SETS:
        slug=s['slug']
        pdf=OUT/f"EIKEN_Grade2_{slug}_Reading_Practice_20260912.pdf"
        docx=OUT/f"EIKEN_Grade2_{slug}_Reading_Practice_20260912.docx"
        if not pdf.exists() or not docx.exists():
            failures.append(f"{slug}: missing DOCX or PDF")
            continue
        d=fitz.open(pdf)
        page_text=[p.get_text("text") for p in d]
        report[slug]={'pages':len(d),'page_sizes':[],'blank_pages':[]}
        for i,p in enumerate(d):
            rect=p.rect
            report[slug]['page_sizes'].append([round(rect.width,2),round(rect.height,2)])
            if abs(rect.width-a4w)>0.8 or abs(rect.height-a4h)>0.8:
                failures.append(f"{slug}: PDF page {i+1} not A4: {rect.width}x{rect.height}")
            if len(re.sub(r"\s+","",page_text[i])) < 25:
                report[slug]['blank_pages'].append(i+1)
                failures.append(f"{slug}: suspicious blank page {i+1}")
        if len(d) < 13:
            failures.append(f"{slug}: unexpectedly short PDF ({len(d)} pages)")
        # cover + exact nine-page problem model
        expected={
            1:[1,5], 2:[6,10], 3:[11,15], 4:[16,17],
            5:[18,20], 6:[21,23], 7:[24,26], 9:[27,31]
        }
        if len(d) >= 10:
            for problem_page,(a,b) in expected.items():
                text=page_text[problem_page]  # zero-based: cover is page 0
                for n in range(a,b+1):
                    if f"({n})" not in text:
                        failures.append(f"{slug}: expected ({n}) on problem page R{problem_page}, PDF page {problem_page+1}")
        full='\n'.join(page_text)
        forbidden=['教材メモ',"Teacher's Note",'正答位置チェック','OBJECTIVE FORMAT CHECK']
        for bad in forbidden:
            if bad in full:
                failures.append(f"{slug}: forbidden student-facing text present: {bad}")
        if 'FULL JAPANESE TRANSLATION' not in full or '全文和訳' not in full:
            failures.append(f"{slug}: missing full Japanese translation section")
        last=page_text[-1]
        if not any(t[-25:] in last for t in s['part3b']['translation'][-1:]):
            # text extraction can wrap, use a normalized tail check
            normlast=re.sub(r"\s+","",last)
            normtail=re.sub(r"\s+","",s['part3b']['translation'][-1])[-20:]
            if normtail not in normlast:
                failures.append(f"{slug}: final PDF page does not appear to end with final translation")
        # Render all pages for visual inspection.
        render_dir=OUT/f"{slug}_render"
        render_dir.mkdir(exist_ok=True)
        for i,p in enumerate(d):
            pix=p.get_pixmap(matrix=fitz.Matrix(1.7,1.7),alpha=False)
            pix.save(render_dir/f"page-{i+1:02d}.png")
        d.close()
    (OUT/'pdf_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    if failures:
        print("PDF AUDIT FAILURES:")
        for x in failures: print("-",x)
        raise SystemExit(1)


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--content-only',action='store_true')
    ap.add_argument('--pdf',action='store_true')
    args=ap.parse_args()
    if args.content_only: check_content()
    elif args.pdf: check_pdfs()
    else:
        check_content(); check_pdfs()
