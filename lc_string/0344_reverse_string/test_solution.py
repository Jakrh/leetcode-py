#!/usr/bin/env python3

from .solution import Solution
import unittest
from dataclasses import dataclass
from typing import Type


class TestReverseString(unittest.TestCase):

    @dataclass
    class Args:
        s: list[str]

    @dataclass
    class TestCase:
        name: str
        args: "TestReverseString.Args"
        expected: list[str]

    @classmethod
    def setUpClass(cls: Type["TestReverseString"]) -> None:
        cls.sol = Solution()
        cls.cases = [
            cls.TestCase("empty", cls.Args([]), []),
            cls.TestCase("single_char", cls.Args(["x"]), ["x"]),
            cls.TestCase("even_length", cls.Args(list("hello!")), list("!olleh")),
            cls.TestCase("odd_length", cls.Args(list("LeetCode")), list("edoCteeL")),
            cls.TestCase("palindrome", cls.Args(list("madam")), list("madam")),
            cls.TestCase(
                "with_duplicates",
                cls.Args(["a", "b", "a", "b", "a"]),
                ["a", "b", "a", "b", "a"],
            ),
            cls.TestCase(
                "long_string",
                cls.Args(list("abcdefghijklmnopqrstuvwxyz")),
                list("zyxwvutsrqponmlkjihgfedcba"),
            ),
            cls.TestCase(
                "special_characters",
                cls.Args([" ", "\t", "\n", "!", "@", "#"]),
                ["#", "@", "!", "\n", "\t", " "],
            ),
            cls.TestCase(
                "numeric_characters",
                cls.Args(["1", "2", "3", "4", "5"]),
                ["5", "4", "3", "2", "1"],
            ),
            cls.TestCase(
                "unicode_characters",
                cls.Args(["ü", "ñ", "字", "😊"]),
                ["😊", "字", "ñ", "ü"],
            ),
            cls.TestCase(
                "mixed_case",
                cls.Args(list("AaBbCcDd")),
                list("dDcCbBaA"),
            ),
        ]

    def test_reverse_string(self):
        for case in self.cases:
            with self.subTest(case=case.name):
                s = case.args.s
                self.sol.reverseString(s)
                self.assertEqual(s, case.expected)


if __name__ == "__main__":
    unittest.main()
