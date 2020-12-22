#! /usr/bin/python3
import sys


def usage():
    """
    Writes the usage string to stdout.
    """
    # this isn't a pretty string, but this way it is the easiest to understand how it will look in a terminal
    sys.stdout.write(
"""Usage: arch [OPTION]...
Print machine architecture.

      --help     display this help and exit
      --version  output version information and exit""")


if __name__ == "__main__":
    if "--help" in sys.argv:
        usage()
    elif len(sys.argv) > 1:
        sys.stderr.out("Too many arguments")
        sys.stderr.write("Usage: sarch")
    else:
        # it's important to use `platform.machine()` in order to have better support in different archs
