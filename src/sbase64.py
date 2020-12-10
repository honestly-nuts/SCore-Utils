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
    # Read from stdin and convert it to bytes if no file is specified
    if len(sys.argv) == 1:
        input_bytes = sys.stdin.read().encode()
    else:
        with open(sys.argv[1], "rb") as file:
            input_bytes = file.read()

    # Base 64 encode the bytes then turn the output into a string
    output = base64.b64encode(input_bytes).decode()

    # Write the output to stdout
    if wrap_columns == 0:
        sys.stdout.write(output)
    else:
        # Keep the output within the specified column width
        while output:
            sys.stdout.write(output[:wrap_columns] + "\n")
            output = output[wrap_columns:]


def decode(wrap_columns, ignore_garbage):
    if len(sys.argv) == 1:
        input_bytes = sys.stdin.read().encode()
    else:
        with open(sys.argv[1], "rb") as file:
            input_bytes = file.read()

    if ignore_garbage:
        while input_bytes:
            try:
                base64.b64decode(input_bytes[:24])
            except binascii.Error:
                pass
            input_bytes = input_bytes[24:]
    else:
        output = base64.b64decode(input_bytes).decode()

    if wrap_columns == 0:
        sys.stdout.write(output)
    else:
        while output:
            sys.stdout.write(output[:wrap_columns])
            output = output[wrap_columns:]


if __name__ == "__main__":
    # Incorrect arguments
    if len(sys.argv) > 5:
        sys.stderr.out("Too many arguments")
        sys.stderr.write("Usage: sbase64 [options] [file]")
        sys.exit()

    if "--help" in sys.argv:
        usage()
        sys.exit()

    # Set output width
    if "-c" in sys.argv:
        cols_index = sys.argv.index("-c")
        wrap_col_number = sys.argv[cols_index + 1]
        sys.argv.remove("-c")
        sys.argv.remove(wrap_col_number)
    else:
        wrap_columns = 76

    if "-d" in sys.argv:
        sys.argv.remove("-d")
        if "-i" in sys.argv:
            sys.argv.remove("-i")
            ignore_garbage = True
        else:
            ignore_garbage = False
        decode(wrap_columns, ignore_garbage)
    else:
        encode(wrap_columns)
