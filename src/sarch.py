#! /usr/bin/python3
import sys


def usage():
    print(
        """Usage: arch
    Prints operating system architecture"""
    )


if __name__ == "__main__":
    if "--help" in sys.argv:
        usage()
    elif len(sys.argv) > 1:
        sys.stderr.out("Too many arguments")
        sys.stderr.write("Usage: sarch")
    else:
        # Determine system architecture using the max integer size
        if sys.maxsize > 2 ** 32:
            sys.stdout.write("x86_64\n")
        else:
            sys.stdout.write("x86\n")
