#!/usr/bin/env python3
"""One-time prompt integration; does not validate the semantics of generated items."""
from pathlib import Path
import argparse
import hashlib
import json
import re

MARK = '<!-- DISTRACTOR-DESIGN-V1 -->'
EXPECTED = {
    'AGENTS.md': 'cb1cf3a99d12440ee12b5fdd9e7b05c190981bce',
    'README.md': '8472ef761b715d0e954e76955b2fcaee0749443f',
    'MASTER_PROMPT.md': '6e8098747f21d4fa0cdd9dcff60f98535f1e7b05',
}
DOCUMENTS = {
    'rules/DISTRACTOR_DESIGN.md': '0d829a8cee8b63706bc6455d492a45690e266f7cc245af8d74865a4c19cc8c50',
    'references/OFFICIAL_DISTRACTOR_CASEBOOK.md': 'd0ac2c57246c16cd84c6767f9806427182c987b4c2e70bac6697685fcb59bb9b',
}
BANNER = '''
<!-- DISTRACTOR-DESIGN-V1 -->
> **選択肢作成前の必須参照：** `rules/DISTRACTOR_DESIGN.md` と `references/OFFICIAL_DISTRACTOR_CASEBOOK.md` を全文読む。公式の観測事例と独自の設計基準を区別し、各候補の本文根拠・もっともらしい理由・決定的なずれ・問いへの適合を確認する。未読・未確認のまま候補を確定しない。既定のレイアウト、SOURCE-FIRST、自然な全訳は維持する。
'''
NEW_POSITION = '''# 9. 正答位置

正答位置の回数・連続・周期を出力前に記録する。ただし均等配分や3連続禁止を公式の規則とは扱わず、回数差が1を超えることや3連続だけで自動不合格にしない。公式正答表の反例は `references/OFFICIAL_DISTRACTOR_CASEBOOK.md` を参照する。

意味と一意性を先に固定し、露骨な周期を意図的に作らない。必要なら候補順を調整するが、意味上の自然順は尊重する。正解内容を番号分散のため変えてはいけない。配置後は安定した選択肢IDから正答番号・解説・和訳を再生成し、必ず再QAする。

ユーザーが均等配分を明示指定した場合だけ教育用の追加条件として適用し、公式の要件とは説明しない。内部の正答分布表は最終教材には掲載しない。

---

'''
PATCHES = [
    ('# 7. 誤答選択肢\n', '# 7. 誤答選択肢\n\n`rules/DISTRACTOR_DESIGN.md` と `references/OFFICIAL_DISTRACTOR_CASEBOOK.md` を必須とする。本節の本文情報を材料にする規則は長文を中心に適用する。Part 1の語義・語法・コロケーションの検査は同規則の専用節に従い、すべてを近義語同士の比較にしない。各候補の根拠、もっともらしい理由、決定的なずれ、問いへの適合を記録し、最も近い誤答も最終本文から排除できるようにする。\n'),
    ('## QA-6 正答位置\n\n- 回数差1以内\n- 3連続なし\n- 露骨な周期なし\n- 正答表と実際の正解が一致', '## QA-6 正答位置\n\n- 回数・連続・周期を内部点検し、意図的な正答の目印を作っていない\n- 均等配分や3連続禁止を公式要件と誤認していない\n- 配置調整後の選択肢IDと正答表・解説・和訳が一致\n- 明示された追加の教育用配分条件がある場合は、それと区別して照合'),
    ('- 正答位置が偏っている\n', '- 選択肢の配置調整後に正答表・解説・和訳との不一致が残る、または必要な再QAをしていない\n'),
]

def blob(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

def install(root):
    originals = {name: (root / name).read_bytes() for name in EXPECTED}
    applied = [MARK in data.decode('utf-8') for data in originals.values()]
    if any(applied):
        if not all(applied) or not all((root / p).is_file() for p in DOCUMENTS):
            raise RuntimeError('Partial integration: review before retrying')
        return []  # Do not overwrite later edits on a repeated run.
    for name, expected in DOCUMENTS.items():
        if hashlib.sha256((root / name).read_bytes()).hexdigest() != expected:
            raise RuntimeError('Analysis document changed: ' + name)
    pending = {}
    for name, original in originals.items():
        if blob(original) != EXPECTED[name]:
            raise RuntimeError('Source changed; reconcile first: ' + name)
        text = original.decode('utf-8')
        changed = text
        if name == 'MASTER_PROMPT.md':
            if changed.count('# 9. 正答位置\n') != 1 or changed.count('# 10. Vocabulary Support') != 1:
                raise RuntimeError('Section anchors changed')
            start = changed.index('# 9. 正答位置\n')
            end = changed.index('# 10. Vocabulary Support', start)
            changed = changed[:start] + NEW_POSITION + changed[end:]
            for old, new in PATCHES:
                if changed.count(old) != 1:
                    raise RuntimeError('Replacement anchor is not unique')
                changed = changed.replace(old, new, 1)
            for forbidden in ['- 回数差1以内', '- 3連続なし', '- 正答位置が偏っている', '同じ番号を3問以上連続させない。', '- 31問：8・8・8・7']:
                assert forbidden not in changed, forbidden
        head, sep, rest = changed.partition('\n')
        if not sep:
            raise RuntimeError('Missing title: ' + name)
        changed = head + '\n' + BANNER + '\n' + rest
        if re.findall(r'^# \d+\.', text, flags=re.M) != re.findall(r'^# \d+\.', changed, flags=re.M):
            raise RuntimeError('Numbered master sections were lost')
        pending[name] = changed.encode('utf-8')
    # Preflight all files before writing anything.
    for name, data in pending.items():
        (root / name).write_bytes(data)
    for name, expected in pending.items():
        assert (root / name).read_bytes() == expected, name
    return sorted(pending)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', default='.')
    args = parser.parse_args()
    root = Path(args.root)
    protected_names = ['LAYOUT_MASTER_PROMPT.md', 'references/EIKEN_G2_LAYOUT_REFERENCE.md', 'rules/FAMOUS_EPISODE_POLICY.md', 'rules/NATURAL_JAPANESE_TRANSLATION.md']
    protected = {name: hashlib.sha256((root / name).read_bytes()).hexdigest() for name in protected_names}
    changed = install(root)
    assert install(root) == [], 'Idempotence failed'
    for name, sha in protected.items():
        assert hashlib.sha256((root / name).read_bytes()).hexdigest() == sha, name
    print(json.dumps({'changed_files': changed, 'idempotent': True, 'protected_files_unchanged': protected_names, 'generated_question_semantics': 'not tested; no new questions generated'}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
