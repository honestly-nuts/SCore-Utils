#! /bin/python3.8
import getpass
import sys


def usage():
    print(
        """Usage: whoami
    Prints the curretn username."""
    )


if __name__ == "__main__":
    if len(sys.argv) > 1:
        usage()
    else:
        sys.stdout.write(getpass.getuser() + "\n")
