#! /bin/python3.8
import sys

def stdinCat():
    while True:
        text = input()
        sys.stdout.write(text)

def fileCat(filename):
    text = ""
    with open(filename, "r") as f:
        text += f.read()
    return text

def cat():
    if len(sys.argv) <= 1:
        stdinCat()
    elif len(sys.argv) >= 2:
        for filename in sys.argv:
            if filename != sys.argv[0]:
                print(fileCat(filename))


if __name__ == '__main__':
    try:
        cat()
    except:
        sys.stdout.write("\n")
        pass
