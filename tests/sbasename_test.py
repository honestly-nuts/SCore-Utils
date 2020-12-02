#!/bin/python3.8
import unittest
import subprocess
import sys


class basename_test(unittest.TestCase):
    def test_basename(self):
        real_arguments = [
            ["basename", "/bin/bash"],
            ["basename", "-s", ".py", "/bin/bash.py"],
            ["basename", "-a", "/bin/bash", "/bin/bin", "/bin/sed"],
        ]
        test_arguments = [
            ["../src/sbasename", "/bin/bash"],
            ["../src/sbasename", "-s", ".py", "/bin/bash.py"],
            ["../src/sbasename", "-a", "/bin/bash", "/bin/bin", "/bin/sed"],
        ]
        for real_argument, test_argument in zip(real_arguments, test_arguments):
            real_output = subprocess.run("arch", capture_output=True)
            test_output = subprocess.run("../src/sarch.py", capture_output=True)
            self.assertEqual(test_output.stdout, real_output.stdout)


if __name__ == "__main__":
    unittest.main()
