#!/usr/bin/env python3
"""Write the front page of Saturday 21 November 2026 to /output/entry.png.

The entry image is the newspaper front page "THE DAILY RECORD" for
Saturday 21 November 2026, drawn with PIL by build_image.py and stored
in this repository as entry.png. This program does the one job the
competition asks of it: it copies that image to the output path, so the
judge sees exactly the bytes the repository holds.

It uses only the Python standard library. The output directory comes
from MAKEFUN_OUTPUT_DIR when set, and defaults to /output otherwise.
The copy is verified: after writing, the program re-reads the output
and refuses to exit quietly if the bytes differ from the source.
"""
import hashlib
import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
OUTPUT_NAME = "entry.png"
MAX_BYTES = 1_048_576  # competition cap: the image must fit in 1 MiB


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    if not source.is_file():
        print(f"error: {SOURCE_NAME} is missing next to main.py",
              file=sys.stderr)
        return 1
    if source.stat().st_size > MAX_BYTES:
        print(f"error: {SOURCE_NAME} is {source.stat().st_size} bytes, "
              f"over the {MAX_BYTES}-byte limit", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / OUTPUT_NAME
    shutil.copyfile(source, target)
    if sha256_of(source) != sha256_of(target):
        print("error: copied bytes differ from the source image",
              file=sys.stderr)
        return 1
    print(f"wrote {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
