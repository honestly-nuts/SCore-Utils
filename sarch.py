#! /bin/python3.8
import sys


def usage():
    print(
        """Usage: arch
    Prints operating system architecture"""
    )


if __name__ == "__main__":
    if "--help" in sys.argv:
        usage()
    else:
        if sys.maxsize > 2 ** 32:
            sys.stdout.write("x86_64\n")
        else:
            sys.stdout.write("x86\n")
