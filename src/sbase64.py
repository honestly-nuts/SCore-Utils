#! /usr/bin/python3
import sys
import base64
import binascii
import argparse


def encode(wrap_columns):
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
    parser = argparse.ArgumentParser(
        description="base64 encodes or decodes a file or standard input"
    )
    parser.add_argument(
        "-w", "--wrap-cols", type=int, default=76, help="wrap encoded line after COLS"
    )
    parser.add_argument(
        "-d", "--decode", action="store_true", help="Decodes base64 to text"
    )
    parser.add_argument(
        "-i",
        "--ignore-garbage",
        action="store_true",
        default=False,
        help="when decoding, ignore non-alphabet characters",
    )

    args = parser.parse_args()

    if args.decode:
        decode(args.wrap_cols, args.ignore_garbage)
    else:
        encode(args.wrap_cols)
