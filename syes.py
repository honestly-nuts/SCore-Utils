#!/usr/bin/env python3
import sys

def main():
    buf = "y"
    if len(sys.argv) >= 2:
        buf = ""
        for arg in sys.argv:
            if arg != sys.argv[0]:
                if arg != sys.argv[1]:
                    buf += " "
                buf += arg

    while True:
        print(buf)

if __name__ == "__main__":
    main()
