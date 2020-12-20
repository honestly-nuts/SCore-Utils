#! /usr/bin/python3
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.stdout.write(" ".join(os.listdir("./")) + "\n")
    else:
        if os.path.isdir(sys.argv[1]):
            sys.stdout.write(" ".join(os.listdir(sys.argv[1])) + "\n")
        else:
            sys.stderr.write(f"{sys.argv[1]} is not a directory\n")
            sys.exit()
