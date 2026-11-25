"""Copy entry.txt byte-identically to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. No temp file, no network, no reading anything outside this
directory. The output file is written directly with mode 0644 so the
grader can read it as another user.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(here, "entry.txt"), "rb") as f:
            data = f.read()
    except OSError as exc:
        print("cannot read entry.txt: %s" % exc, file=sys.stderr)
        return 1
    if not data.strip():
        print("entry.txt is empty or whitespace only", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "wb") as f:
            f.write(data)
        os.chmod(out_path, 0o644)
    except OSError as exc:
        print("cannot write output: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
