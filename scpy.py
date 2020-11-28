#!/bin/python3.8

def copy(filenames):
    text = ""
    for filename in filenames:
        with open(filename, "r") as f:
            text += f.read()
    return text

def paste(text, filename):
    with open(filename, "w"):
        f.write(text)


if __name__ == "__main__":
    text = copy(sys.argv[1:-1])
    paste(text, sys.argv[-1])
