#!/bin/python3.8
import unittest
import subprocess
import sys


class base64_test(unittest.TestCase):
    def test_encode(self):
        test_string = "abcdefghijklmnopqrstuvwxyz".encode()
        real_output = subprocess.run("base64", capture_output=True, input=test_string)
        test_output = subprocess.run(
            "../src/sbase64.py", capture_output=True, input=test_string
        )
        self.assertEqual(test_output.stdout, real_output.stdout)

    def test_decode(self):
        test_string = "YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXoK".encode()
        real_output = subprocess.run(
            ["base64", "-d"], capture_output=True, input=test_string
        )
        test_output = subprocess.run(
            ["../src/sbase64.py", "-d"], capture_output=True, input=test_string
        )
        self.assertEqual(test_output.stdout, real_output.stdout)


if __name__ == "__main__":
    unittest.main()
