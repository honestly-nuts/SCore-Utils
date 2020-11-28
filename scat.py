#! /bin/python3.8
import sys

if len(sys.argv) < 2:
    print("Usage: filenames")
    sys.exit()
def cat():
    text = ''
    for filename in sys.argv:
        if (filename != sys.argv[0]):
            with open(filename, "r") as f:
                text += f.read()
    print(text)


if __name__ == '__main__':
    cat()
