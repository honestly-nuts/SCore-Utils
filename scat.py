#! /bin/python3.8
import sys

def cat():
    if len(sys.argv) < 2:
        while True:
            text = input()
            print(text)
    else:
        text = ''
        for filename in sys.argv:
            if (filename != sys.argv[0]):
                with open(filename, "r") as f:
                    sys.stdout.write(f.read())

if __name__ == '__main__':
    try:
        cat()
    except:
        pass
