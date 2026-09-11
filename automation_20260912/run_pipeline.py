import argparse

import data
from patches import apply_patches

apply_patches(data.SETS)

import audit
import generate


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
