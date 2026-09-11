from pathlib import Path
from copy import deepcopy
from docx import Document
from docx.shared import Mm, Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.style import WD_STYLE_TYPE
from PIL import Image, ImageDraw

from data import SETS

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "automation-20260912"
OUT.mkdir(parents=True, exist_ok=True)

SERIF = "Liberation Serif"
SANS = "Liberation Sans"
JP_SERIF = "Noto Serif CJK JP"
JP_SANS = "Noto Sans CJK JP"

SAFE_FRONT = {
    "detective_conan_moonlight": {
        "intro_jp": "『名探偵コナン』は、少年の姿になった高校生探偵が数々の事件に挑むミステリー作品です。今回は、月影島に届いた不可解な依頼から始まる『月光』事件を題材にします。作品を知らなくても、問題に必要な情報は本文中に示してあります。",
        "background_en": "Conan, Ran, and Kogoro travel to Moonshade Island after a letter asks them to investigate a strange matter. The request is unusual because the person named as the client is a pianist who was said to have died twelve years earlier while playing Beethoven's Moonlight Sonata. On the island, a memorial service for the previous mayor is being held at a community center. During the gathering, the same piece of music is heard. The case becomes more serious when the current mayor is found dead and a musical score written in blood appears. This practice set uses these events as the factual background for original English reading tasks. Everything needed to answer the questions is stated in the passages, so prior knowledge of the series is not required.",
    },
    "fullmetal_alchemist_origin": {
        "intro_jp": "『鋼の錬金術師』は、錬金術が存在する世界で、エドワードとアルフォンスの兄弟が旅を続ける物語です。今回は、兄弟の錬金術が失敗した後、失った身体を取り戻す方法を求めて動き始める物語の出発点を扱います。必要な設定は本文中で説明します。",
        "background_en": "Edward and Alphonse Elric are brothers who use alchemy in an attempt to fulfill an important wish, but the ritual goes terribly wrong. Edward loses an arm and a leg, while Alphonse becomes a soul inside a suit of armor. Edward later uses mechanical auto-mail limbs and becomes a State Alchemist. The brothers then search for the legendary Philosopher's Stone because they hope it may help them restore their bodies. The events in this practice set are based on the manga series' established premise, but all English passages and questions are original. Readers do not need prior knowledge of the manga or anime; the information required for each answer appears in the passage itself.",
    },
    "sailor_moon_episode1": {
        "intro_jp": "『美少女戦士セーラームーン』は、中学生の月野うさぎが黒猫ルナとの出会いをきっかけに、セーラームーンとして歩み始める作品です。今回は、うさぎがルナと出会い、変身ブローチを受け取り、初めて新しい力を使う第1話を題材にします。必要な背景は本文中に示しています。",
        "background_en": "Usagi Tsukino is an ordinary fourteen-year-old schoolgirl when she meets Luna, a black cat marked with a crescent moon. Usagi first helps the cat when some children are bothering her. Later, Luna comes to Usagi and gives her a special brooch that allows her to transform into Sailor Moon. Luna also tells Usagi about a mission involving the Moon Princess and other Guardians. Soon afterward, Usagi hears a friend calling for help. This practice set uses the sequence of these first-episode events as the factual background for original English reading tasks. Students do not need to know the series in advance because every fact needed to answer the questions is provided in the passages.",
    },
}


def set_cell_margins(cell, top=70, start=90, bottom=70, end=90):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMar = tcPr.first_child_found_in("w:tcMar")
    if tcMar is None:
        tcMar = OxmlElement("w:tcMar")
        tcPr.append(tcMar)
    for m, v in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tcMar.find(qn(f"w:{m}"))
        if node is None:
            node = OxmlElement(f"w:{m}")
            tcMar.append(node)
        node.set(qn("w:w"), str(v))
        node.set(qn("w:type"), "dxa")


def no_split(row):
    trPr = row._tr.get_or_add_trPr()
    cant = OxmlElement("w:cantSplit")
    trPr.append(cant)


def keep(p, nxt=False):
    pf = p.paragraph_format
    pf.keep_together = True
    pf.keep_with_next = nxt


def set_run_font(run, latin=SERIF, east=JP_SERIF, size=12.5, bold=False, italic=False):
    run.font.name = latin
    run._element.rPr.rFonts.set(qn("w:ascii"), latin)
    run._element.rPr.rFonts.set(qn("w:hAnsi"), latin)
    run._element.rPr.rFonts.set(qn("w:eastAsia"), east)
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic


def set_p(p, before=0, after=0, line=15.5, align=None, first=0):
    f = p.paragraph_format
    f.space_before = Pt(before)
    f.space_after = Pt(after)
    f.line_spacing = Pt(line)
    if first:
        f.first_line_indent = Mm(first)
    if align is not None:
        p.alignment = align


def add_text(p, text, *, latin=SERIF, east=JP_SERIF, size=12.5, bold=False, italic=False):
    r = p.add_run(text)
    set_run_font(r, latin, east, size, bold, italic)
    return r


def shade_cell(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = tcPr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tcPr.append(shd)
    shd.set(qn("w:fill"), fill)


def border_cell(cell, val="single", sz="6", color="808080"):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = tcPr.first_child_found_in("w:tcBorders")
    if borders is None:
        borders = OxmlElement("w:tcBorders")
        tcPr.append(borders)
    for edge in ["top", "left", "bottom", "right", "insideH", "insideV"]:
        tag = f"w:{edge}"
        el = borders.find(qn(tag))
        if el is None:
            el = OxmlElement(tag)
            borders.append(el)
        el.set(qn("w:val"), val)
        el.set(qn("w:sz"), sz)
        el.set(qn("w:color"), color)


def add_page_number(paragraph):
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = paragraph.add_run("Unofficial Grade 2 Reading Practice  |  ")
    set_run_font(r, SANS, JP_SANS, 8.5)
    r = paragraph.add_run()
    fldChar1 = OxmlElement("w:fldChar"); fldChar1.set(qn("w:fldCharType"), "begin")
    instrText = OxmlElement("w:instrText"); instrText.set(qn("xml:space"), "preserve"); instrText.text = " PAGE "
    fldChar2 = OxmlElement("w:fldChar"); fldChar2.set(qn("w:fldCharType"), "end")
    r._r.append(fldChar1); r._r.append(instrText); r._r.append(fldChar2)
    set_run_font(r, SANS, JP_SANS, 8.5)


def page_break(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    p.add_run().add_break()
    p.runs[-1]._r.get_or_add_br().set(qn("w:type"), "page")


def configure(doc):
    sec = doc.sections[0]
    sec.page_width = Mm(210)
    sec.page_height = Mm(297)
    sec.top_margin = Mm(15)
    sec.bottom_margin = Mm(15)
    sec.left_margin = Mm(18)
    sec.right_margin = Mm(18)
    sec.header_distance = Mm(7)
    sec.footer_distance = Mm(7)
    add_page_number(sec.footer.paragraphs[0])
    normal = doc.styles["Normal"]
    normal.font.name = SERIF
    normal._element.rPr.rFonts.set(qn("w:ascii"), SERIF)
    normal._element.rPr.rFonts.set(qn("w:hAnsi"), SERIF)
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), JP_SERIF)
    normal.font.size = Pt(12.5)


def make_icon(slug, dest):
    img = Image.new("L", (1500, 420), 255)
    d = ImageDraw.Draw(img)
    if "conan" in slug:
        d.ellipse((160, 80, 390, 310), outline=60, width=14)
        d.line((350, 270, 510, 390), fill=60, width=18)
        d.line((650, 95, 650, 280), fill=80, width=16)
        d.arc((650, 220, 770, 340), 0, 300, fill=80, width=16)
        d.line((650, 95, 790, 70), fill=80, width=16)
    elif "fullmetal" in slug:
        d.ellipse((180, 55, 520, 395), outline=70, width=12)
        d.ellipse((250, 125, 450, 325), outline=130, width=6)
        d.polygon([(350,80),(465,300),(235,300)], outline=90)
        d.line((780,100,780,310), fill=70, width=28)
        d.line((780,145,930,220), fill=70, width=24)
        d.line((780,145,650,225), fill=70, width=24)
        d.ellipse((725,300,835,410), outline=70, width=20)
    else:
        d.arc((180,45,500,365), 55, 305, fill=60, width=28)
        d.arc((260,45,580,365), 55, 305, fill=255, width=58)
        d.ellipse((760,130,940,310), outline=70, width=12)
        d.polygon([(785,145),(810,65),(855,145)], fill=220, outline=70)
        d.polygon([(845,145),(900,65),(920,155)], fill=220, outline=70)
        d.line((850,300,850,395), fill=70, width=12)
        d.arc((920,245,1080,405), 190, 350, fill=70, width=12)
    img.save(dest)


def add_band(doc, part, subtitle=""):
    t = doc.add_table(rows=1, cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    t.columns[0].width = Mm(31)
    t.columns[1].width = Mm(136)
    c1, c2 = t.rows[0].cells
    shade_cell(c1, "333333"); shade_cell(c2, "E6E6E6")
    set_cell_margins(c1, 60, 120, 60, 120); set_cell_margins(c2, 60, 120, 60, 120)
    p = c1.paragraphs[0]; set_p(p, line=16); add_text(p, part, latin=SANS, east=JP_SANS, size=13, bold=True); p.runs[0].font.color.rgb = None
    p = c2.paragraphs[0]; set_p(p, line=16); add_text(p, subtitle, latin=SANS, east=JP_SANS, size=11.5, bold=True)
    return t


def question_table(doc, item, phrase=False):
    rows = 3 if phrase else 2
    t = doc.add_table(rows=rows, cols=4)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    widths = [Mm(42)]*4
    for i,w in enumerate(widths): t.columns[i].width=w
    stemcell = t.rows[0].cells[0]
    for c in t.rows[0].cells[1:]: stemcell = stemcell.merge(c)
    p0 = t.rows[0].cells[0].paragraphs[0]
    set_p(p0, before=1, after=2, line=15.2)
    add_text(p0, f"({item['num']})  {item['stem']}", size=12.3)
    no_split(t.rows[0])
    if not phrase:
        for i,ch in enumerate(item['choices']):
            p = t.rows[1].cells[i].paragraphs[0]; set_p(p, after=1, line=14.6)
            add_text(p, f"{i+1}  {ch}", size=11.9)
            set_cell_margins(t.rows[1].cells[i], 20, 70, 40, 70)
        no_split(t.rows[1])
    else:
        pairs = [(0,1),(2,3)]
        for ridx, pair in enumerate(pairs, start=1):
            for colidx, ci in enumerate(pair):
                c = t.rows[ridx].cells[colidx*2]
                c = c.merge(t.rows[ridx].cells[colidx*2+1])
                p = c.paragraphs[0]; set_p(p, after=1, line=14.6)
                add_text(p, f"{ci+1}  {item['choices'][ci]}", size=11.9)
                set_cell_margins(c, 20, 70, 40, 70)
            no_split(t.rows[ridx])
    doc.add_paragraph().paragraph_format.space_after = Pt(1)


def add_part1_page(doc, items, label):
    add_band(doc, "1", f"Short Vocabulary / Phrase Questions  {label}")
    p = doc.add_paragraph(); set_p(p, before=5, after=6, line=14.5)
    add_text(p, "Choose the best word or phrase for each blank.", size=11.6, italic=True)
    for it in items:
        question_table(doc, it, phrase=it['num'] >= 11)


def add_passage(doc, part_label, passage, qnums):
    add_band(doc, "2", part_label)
    p = doc.add_paragraph(); set_p(p, before=5, after=6, line=14.5)
    add_text(p, "Choose the best answer for each blank in the passage.", size=11.6, italic=True)
    title = doc.add_paragraph(); set_p(title, before=2, after=6, line=22, align=WD_ALIGN_PARAGRAPH.CENTER)
    add_text(title, passage['title'], size=19.5, italic=True)
    for para in passage['paragraphs']:
        p = doc.add_paragraph(); set_p(p, after=3.5, line=15.2, first=5)
        add_text(p, para, size=12.1)
    for item in passage['questions']:
        question_table(doc, item, phrase=max(len(c) for c in item['choices']) < 25)


def add_email(doc, block):
    add_band(doc, "3", "A  E-mail Reading Comprehension")
    p = doc.add_paragraph(); set_p(p, before=4, after=4, line=14)
    add_text(p, "Read the e-mail and answer questions (24)–(26).", size=11.5, italic=True)
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.cell(0,0); border_cell(c, color="777777"); set_cell_margins(c, 100, 150, 100, 150)
    for key,val in block['headers'].items():
        p = c.add_paragraph() if c.paragraphs[0].text else c.paragraphs[0]
        set_p(p, after=1, line=13.7)
        add_text(p, f"{key}: ", latin=SANS, east=JP_SANS, size=10.9, bold=True)
        add_text(p, val, latin=SANS, east=JP_SANS, size=10.9)
    p = c.add_paragraph(); set_p(p, before=3, after=2, line=13.7); add_text(p, block['greeting'], latin=SANS, east=JP_SANS, size=10.9)
    for para in block['paragraphs']:
        p = c.add_paragraph(); set_p(p, after=2.5, line=13.7); add_text(p, para, latin=SANS, east=JP_SANS, size=10.9)
    p = c.add_paragraph(); set_p(p, before=2, line=13.7); add_text(p, block['closing'], latin=SANS, east=JP_SANS, size=10.9)
    no_split(t.rows[0])
    for it in block['questions']:
        question_table(doc, it, phrase=True)


def add_part3b_text(doc, block):
    add_band(doc, "3", "B  Reading Comprehension")
    title = doc.add_paragraph(); set_p(title, before=7, after=7, line=22, align=WD_ALIGN_PARAGRAPH.CENTER)
    add_text(title, block['title'], latin=SANS, east=JP_SANS, size=19.5, italic=True)
    for para in block['paragraphs']:
        p = doc.add_paragraph(); set_p(p, after=5, line=15.6, first=5)
        add_text(p, para, size=12.3)


def add_part3b_questions(doc, block):
    add_band(doc, "3", "B  Questions")
    p=doc.add_paragraph(); set_p(p,before=5,after=5,line=14); add_text(p,"Choose the best answer for each question.",size=11.5,italic=True)
    for it in block['questions']:
        question_table(doc, it, phrase=True)


def add_cover(doc, s):
    sf = SAFE_FRONT[s['slug']]
    p=doc.add_paragraph(); set_p(p,after=1,line=20,align=WD_ALIGN_PARAGRAPH.CENTER)
    add_text(p,"EIKEN Grade 2 Reading",latin=SANS,east=JP_SANS,size=15,bold=True)
    p=doc.add_paragraph(); set_p(p,after=2,line=28,align=WD_ALIGN_PARAGRAPH.CENTER)
    add_text(p,s['display_title'],latin=SANS,east=JP_SANS,size=24,bold=True)
    p=doc.add_paragraph(); set_p(p,after=8,line=17,align=WD_ALIGN_PARAGRAPH.CENTER)
    add_text(p,s['jp_title'],latin=SANS,east=JP_SANS,size=13.5,bold=True)
    p=doc.add_paragraph(); set_p(p,before=2,after=2,line=18); add_text(p,"作品について / About the Story",latin=SANS,east=JP_SANS,size=14,bold=True)
    p=doc.add_paragraph(); set_p(p,after=6,line=18); add_text(p,sf['intro_jp'],latin=SERIF,east=JP_SERIF,size=11.8)
    p=doc.add_paragraph(); set_p(p,before=1,after=2,line=17); add_text(p,"Short Story Background",latin=SANS,east=JP_SANS,size=13,bold=True)
    p=doc.add_paragraph(); set_p(p,after=6,line=15.6); add_text(p,sf['background_en'],size=11.8)
    t=doc.add_table(rows=1,cols=2); t.alignment=WD_TABLE_ALIGNMENT.CENTER
    t.autofit=False; t.columns[0].width=Mm(68); t.columns[1].width=Mm(98)
    hdr=t.rows[0].cells; shade_cell(hdr[0],"E6E6E6"); shade_cell(hdr[1],"E6E6E6")
    for c,txt in zip(hdr,["日本語名・用語","English in this booklet"]):
        pp=c.paragraphs[0]; set_p(pp,line=14); add_text(pp,txt,latin=SANS,east=JP_SANS,size=10.8,bold=True)
    for jp,en in s['names']:
        row=t.add_row(); no_split(row)
        for c,txt in zip(row.cells,[jp,en]):
            set_cell_margins(c,40,70,40,70); pp=c.paragraphs[0]; set_p(pp,line=13.2); add_text(pp,txt,latin=SERIF,east=JP_SERIF,size=10.6)
    icon=OUT/f"{s['slug']}_theme.png"; make_icon(s['slug'],icon)
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_before=Pt(5)
    r=p.add_run(); r.add_picture(str(icon),width=Mm(125))


def all_questions(s):
    arr=list(s['part1'])
    arr+=s['part2a']['questions']+s['part2b']['questions']
    arr+=s['part3a']['questions']+s['part3b']['questions']
    return sorted(arr,key=lambda x:x['num'])


def add_answers(doc,s):
    add_band(doc,"ANSWERS","Answer Key")
    qs=all_questions(s)
    t=doc.add_table(rows=1,cols=4); t.alignment=WD_TABLE_ALIGNMENT.CENTER
    for c in t.rows[0].cells: shade_cell(c,"E6E6E6")
    for c,txt in zip(t.rows[0].cells,["Question","Answer","Question","Answer"]):
        p=c.paragraphs[0]; set_p(p,line=14); add_text(p,txt,latin=SANS,east=JP_SANS,size=11,bold=True)
    left=qs[:16]; right=qs[16:]
    for i in range(max(len(left),len(right))):
        row=t.add_row(); no_split(row)
        vals=[]
        for side in (left,right):
            if i<len(side): vals += [str(side[i]['num']),str(side[i]['answer'])]
            else: vals += ["",""]
        for c,txt in zip(row.cells,vals):
            p=c.paragraphs[0]; set_p(p,line=13); add_text(p,txt,size=11)


def add_explanations(doc,s):
    add_band(doc,"EXPLANATIONS","解答・解説")
    for item in all_questions(s):
        t=doc.add_table(rows=1,cols=1); t.alignment=WD_TABLE_ALIGNMENT.CENTER
        c=t.cell(0,0); set_cell_margins(c,60,90,60,90)
        p=c.paragraphs[0]; set_p(p,after=1,line=15)
        add_text(p,f"({item['num']})  正解 {item['answer']}  {item['choices'][item['answer']-1]}",latin=SERIF,east=JP_SERIF,size=11.7,bold=True)
        p=c.add_paragraph(); set_p(p,line=15.2); add_text(p,item['explanation'],latin=SERIF,east=JP_SERIF,size=11.4)
        no_split(t.rows[0])
        gap=doc.add_paragraph(); gap.paragraph_format.space_after=Pt(2)


def add_translation_section(doc,s):
    add_band(doc,"FULL JAPANESE TRANSLATION","全文和訳")
    blocks=[("Part 2A",s['part2a']), ("Part 2B",s['part2b']), ("Part 3A E-mail",s['part3a']), ("Part 3B",s['part3b'])]
    for label,b in blocks:
        p=doc.add_paragraph(); set_p(p,before=7,after=3,line=18); add_text(p,f"{label}  {b.get('title','')}",latin=SANS,east=JP_SANS,size=13.5,bold=True)
        for idx,para in enumerate(b['translation'],1):
            p=doc.add_paragraph(); set_p(p,after=5,line=18,first=4)
            add_text(p,para,latin=SERIF,east=JP_SERIF,size=11.8)


def build(s):
    doc=Document(); configure(doc)
    props=doc.core_properties
    props.title=f"EIKEN Grade 2 Reading - {s['display_title']}"
    props.subject=s['episode_label']
    add_cover(doc,s)
    # Fixed 9-page problem section after the cover.
    groups=[(1,5),(6,10),(11,15),(16,17)]
    for idx,(a,b) in enumerate(groups):
        page_break(doc)
        add_part1_page(doc,[x for x in s['part1'] if a<=x['num']<=b],f"({a})–({b})")
    page_break(doc); add_passage(doc,"A  Passage Cloze",s['part2a'],(18,20))
    page_break(doc); add_passage(doc,"B  Passage Cloze",s['part2b'],(21,23))
    page_break(doc); add_email(doc,s['part3a'])
    page_break(doc); add_part3b_text(doc,s['part3b'])
    page_break(doc); add_part3b_questions(doc,s['part3b'])
    page_break(doc); add_answers(doc,s)
    page_break(doc); add_explanations(doc,s)
    page_break(doc); add_translation_section(doc,s)
    out=OUT/f"EIKEN_Grade2_{s['slug']}_Reading_Practice_20260912.docx"
    doc.save(out)
    print(out)


if __name__ == "__main__":
    for s in SETS:
        build(deepcopy(s))
