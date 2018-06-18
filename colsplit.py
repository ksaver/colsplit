#!/usr/bin/env python3

# ~~~~~~~~~~~
# colsplit.py
# ~~~~~~~~~~~

# Splits a text file in columns.
# Example: ./colsplit.py -c 6 -s "," file.txt
# View README.md for more info.
# ksaver, 16.06.18

import argparse
import sys


def main(args):
    ncols = args.columns
    sep = args.separator
    text = args.filename.read()
    lines = text.split()
    count = 1
    for line in lines:
        if count == ncols:
            print(line, end="\n")
            count = 1
        else:
            print(line, end=sep)
            count += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description = "Splits a text file in columns.")
    parser.add_argument("-c", "--columns", type=int, default=1,
            help="Number of columns.")
    parser.add_argument("-s", "--separator", default="\t",
            help="Separator to use. Default is '\t'.")
    parser.add_argument("filename", default=sys.stdin,
            type=argparse.FileType('r', encoding=('latin-1')),
            help="Text file to split in columns.")
    args = parser.parse_args()

    main(args)
