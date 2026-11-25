"""sample.py 的单元测试，仅用标准库 unittest，无需第三方依赖。"""

import unittest

from sample import add, divide, is_palindrome


class TestAdd(unittest.TestCase):
    def test_integers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative(self):
        self.assertEqual(add(-4, 1), -3)

    def test_floats(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=9)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)


class TestDivide(unittest.TestCase):
    def test_exact(self):
        self.assertEqual(divide(10, 2), 5)

    def test_fraction(self):
        self.assertAlmostEqual(divide(1, 3), 1 / 3, places=12)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

    def test_negative_divisor(self):
        self.assertEqual(divide(9, -3), -3)


class TestPalindrome(unittest.TestCase):
    def test_classic_sentence(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_simple(self):
        self.assertTrue(is_palindrome("level"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("python"))

    def test_case_and_symbols_ignored(self):
        self.assertTrue(is_palindrome("No 'x' in Nixon"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
