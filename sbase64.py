#! /bin/python3.8
import sys
import base64
import binascii


def usage():
    print(
        """Usage: sbase64 [option] [file]
    Base64 encode or decode a file or standard input or output."""
    )


def encode(wrap_cols):
    if len(sys.argv) == 1:
        text = sys.stdin.readlines().encode
    else:
        with open(sys.argv[1], "rb") as file:
            text = file.read()

    output = base64.b64encode(text).decode()
    if wrap_cols == 0:
        sys.stdout.write(output)
    else:
        while output:
            sys.stdout.write(output[:wrap_cols] + "\n")
            output = output[wrap_cols:]


def decode(wrap_cols, ignore_garbage=False):
    if len(sys.argv) == 1:
        text = sys.stdin.read().encode()
    else:
        with open(sys.argv[1], "rb") as file:
            text = file.read()

    if ignore_garbage:
        while text:
            try:
                base64.b64decode(text[:24])
            except binascii.Error:
                pass
            text = text[24:]
    else:
        output = base64.b64decode(text).decode()

    if wrap_cols == 0:
        sys.stdout.write(output)
    else:
        while output:
            sys.stdout.write(output[:wrap_cols] + "\n")
            output = output[wrap_cols:]


if __name__ == "__main__":
    if "--help" in sys.argv:
        usage()
        sys.exit()

    if "-c" in sys.argv:
        cols_index = sys.argv.index("-c")
        wrap_col_number = sys.argv[cols_index + 1]
        sys.argv.remove("-c")
        sys.argv.remove(wrap_col_number)
    else:
        wrap_cols = 76

    if "-d" in sys.argv:
        sys.argv.remove("-d")
        if "-i" in sys.argv:
            sys.argv.remove("-i")
            decode(wrap_cols, ignore_garbage=True)
            sys.exit()
        else:
            decode(wrap_cols)
            sys.exit()
    else:
        encode(wrap_cols)
