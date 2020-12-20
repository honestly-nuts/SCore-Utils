#! /usr/bin/python3
import getpass
import sys



if __name__ == "__main__":
    if len(sys.argv) > 1:
        sys.stderr.write("Too many arguments!\n")
        sys.stderr.write("Usage: swhoami\n")
        sys.exit()

    sys.stdout.write(getpass.getuser() + "\n")
