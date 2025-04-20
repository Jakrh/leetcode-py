#!/usr/bin/env python3

import unittest
import os


def main():
    # Get the current directory of the script
    start_dir = os.path.dirname(os.path.abspath(__file__))

    # Use unittest's TestLoader to discover all test files in the current directory
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir, pattern="test_*.py")

    # Create a test runner that will run the tests
    runner = unittest.TextTestRunner(verbosity=2)  # verbosity=2 equals -v
    runner.run(suite)


if __name__ == "__main__":
    main()
