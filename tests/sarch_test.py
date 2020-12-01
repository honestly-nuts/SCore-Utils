#!/bin/python3.8
import unittest
import subprocess
import sys


class arch_test(unittest.TestCase):
    def test_arch(self):
        real_output = subprocess.run("arch", capture_output=True)
        test_output = subprocess.run("../src/sarch.py", capture_output=True)
        self.assertEqual(test_output.stdout, real_output.stdout)


if __name__ == "__main__":
    unittest.main()
