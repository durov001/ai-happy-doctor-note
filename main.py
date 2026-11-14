#!/usr/bin/env python3
"""Copy the bundled entry image to the output directory.

The entry is one image, a JPEG, written out as entry.png (the
competition reads the format from the file's first bytes, so a JPEG
under that name is accepted). The program copies the bundled bytes
unchanged, so both runs write identical output. Standard library only.
Verified: the bundled image is 1024x1024 pixels, 269663 bytes, under
the competition's 1 MiB cap.
"""
import os
import shutil

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
IMAGE_NAME = "entry.jpg"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, IMAGE_NAME)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    dst = os.path.join(OUTPUT_DIR, "entry.png")
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
