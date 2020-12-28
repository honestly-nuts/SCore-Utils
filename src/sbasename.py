#! /usr/bin/python3
import os
import sys
import re


def usage():
    print(
        """Usage: sbasename [options] name [suffix]
    Prints name with leading directory information and suffix removed.
    Options:
        -a support multiple arguments for name
        -s remove a trailing suffix, implies -a
        -z end each output line with NUL, not newline"""
    )


def extract_name(suffix, terminator):
    if "-a" in sys.argv:
        sys.argv.remove("-a")
        for path in sys.argv[1:]:
            output = re.sub(r"~?\/(\S*\/)*", "", path)
            output = output.strip(suffix)
            sys.stdout.write(output + terminator)

    else:
        output = re.sub(r"~?\/(\S*\/)*", "", sys.argv[1])
        output = output.strip(suffix)
        sys.stdout.write(output + terminator)


if __name__ == "__main__":
    if "--help" in sys.argv:
        usage()
        sys.exit()

    if len(sys.argv) < 2:
        sys.stderr.write("Too few arguments\n")
        sys.stderr.write("Usage: sbasename [options] name [suffix]")
        sys.exit()

    if "-s" in sys.argv:
        suffix = sys.argv[sys.argv.index("-s") + 1]
        sys.argv.remove("-s")
        sys.argv.remove(suffix)
    else:
        suffix = ""

    if "-z" in sys.argv:
        terminator = "\0"
        if "-a" not in sys.argv:
            sys.argv.append("-a")
        sys.argv.remove("-z")
    else:
        terminator = "\n"

    extract_name(suffix, terminator)

