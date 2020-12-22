#! /usr/bin/python3
import sys

def yes(buf="y"):
    sys.stdout.write(buf + "\n")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        sys.stderr.write("Too many arguments!\n")
        sys.stderr.write("Usage: syes (string)\n")
        sys.exit()

    if len(sys.argv) == 1:
        buf = "y"
    else:
        buf = sys.argv[1]

    try:
        while True:
            yes(buf)
    except KeyboardInterrupt:
        sys.exit()
