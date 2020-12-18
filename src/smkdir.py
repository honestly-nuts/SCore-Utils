#! /usr/bin/python3
import os
import sys

if len(sys.argv) == 1:
    sys.stderr.write("Too few arguments\n")
    sys.exit()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if not os.path.exists(sys.argv[1]):
            os.mkdir(sys.argv[1])
    else:
        for arg in sys.argv[1:]:
            if not os.path.exists(arg):
                os.mkdir(arg)
