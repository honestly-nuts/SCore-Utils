#! /usr/bin/python3
import sys


def stdin_cat():
    for line in sys.stdin:
        sys.stdout.write(line)


def file_cat(filename):
    try:
        with open(filename, "r") as f:
            for line in f:
                sys.stdout.write(line)
    except FileNotFoundError:
        sys.stderr.write("File does not exist\n")


def cat():
    if len(sys.argv) >= 2:
        for filename in sys.argv[1:]:
            if filename == "-":
                stdin_cat()
            else:
                file_cat(filename)
    else:
        stdin_cat()


if __name__ == "__main__":
    cat()
