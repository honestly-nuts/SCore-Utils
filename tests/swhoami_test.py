#!/bin/python3.8
import unittest
import subprocess
import sys


class whoami_test(unittest.TestCase):
    def test_user(self):
        real_output = subprocess.run("whoami", capture_output=True)
        test_output = subprocess.run("../src/swhoami.py", capture_output=True)
        self.assertEqual(test_output.stdout, real_output.stdout)


if __name__ == "__main__":
    unittest.main()
