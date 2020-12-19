#! /usr/bin/python3
import sys


def copy(filenames):
    text = ""
    for filename in filenames:
        with open(filename, "r") as f:
            text += f.read()
    return text

def paste(text, filename):
    with open(filename, "w") as f:
        f.write(text)


if __name__ == "__main__":
    if len(sys.argv) <= 2:
        sys.stderr.write("Too few arguments!\n")
        sys.stderr.write("Usage: scpy inputfile(s) outputfile\n")
        sys.exit()

    text = copy(sys.argv[1:-1])
    paste(text, sys.argv[-1])
