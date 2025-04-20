#!/usr/bin/env python3

from .solution import Solution
import unittest
from dataclasses import dataclass
from typing import Type, List


class TestMaxArea(unittest.TestCase):

    @dataclass
    class Args:
        height: List[int]

    @dataclass
    class TestCase:
        name: str
        args: "TestMaxArea.Args"
        expected: int

    @classmethod
    def setUpClass(cls: Type["TestMaxArea"]) -> None:
        cls.sol = Solution()
        cls.cases = [
            cls.TestCase("leetcode-1", cls.Args([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49),
            cls.TestCase("leetcode-2", cls.Args([1, 1]), 1),
            cls.TestCase("empty", cls.Args([]), 0),
            cls.TestCase("1-element", cls.Args([1]), 0),
            cls.TestCase("first-last", cls.Args([1, 2, 3, 4, 5, 6, 7, 8, 9]), 20),
            cls.TestCase("last-first", cls.Args([9, 8, 7, 6, 5, 4, 3, 2, 1]), 20),
            cls.TestCase("positive-negative", cls.Args([5, -1, -2, -3, -4]), 0),
        ]

    def test_maxArea(self):
        for case in self.cases:
            with self.subTest(case=case.name):
                result = self.sol.maxArea(case.args.height)
                self.assertEqual(result, case.expected)


if __name__ == "__main__":
    unittest.main()
