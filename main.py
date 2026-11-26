"""Copy entry.txt into the grader's output directory.

Stdlib only: the grader runs this with no network, a read-only repo,
and only MAKEFUN_OUTPUT_DIR writable.
"""

import os
import shutil

# The joke lives in entry.txt, so this file does nothing clever on
# purpose: it just moves those bytes into the output directory
# untouched, and lets the words do the work.

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.txt")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
