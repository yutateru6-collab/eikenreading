import argparse

import data
from patches import apply_patches

apply_patches(data.SETS)

import audit
import generate
from docx.enum.text import WD_BREAK


def reliable_page_break(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = 0
    p.add_run().add_break(WD_BREAK.PAGE)


generate.page_break = reliable_page_break


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('stage', choices=['content', 'generate', 'pdf'])
    args = ap.parse_args()
    if args.stage == 'content':
        audit.check_content()
    elif args.stage == 'generate':
        for s in data.SETS:
            generate.build(s)
    else:
        audit.check_pdfs()


if __name__ == '__main__':
    main()
