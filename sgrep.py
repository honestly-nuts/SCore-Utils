#! /bin/python3.8
import sys
import re


def grep_file(token):
    for i in sys.argv[2:]:
        with open(i, "r") as fl:
            for line in fl.read().split("\n"):
                if token in line.split(" "):
                    sys.stdout.write(line + "\n")


def grep_stdin(token):
    for line in sys.stdin.read().split("\n"):
        if token in line.split(" "):
            sys.stdout.write(line + "\n")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        grep_stdin(sys.argv[1])
    elif len(sys.argv) >= 3:
        grep_file(sys.argv[1])
    else:
        print("Usage: sgrep.py token file(s)")
        sys.exit()
