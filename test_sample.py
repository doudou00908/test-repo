"""sample.py 的单元测试，仅用标准库 unittest，无需第三方依赖。"""

import math
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

    def test_large_integers(self):
        big = 10**18
        self.assertEqual(add(big, big), 2 * big)

    def test_identity_with_zero(self):
        for value in (0, 7, -3, 2.5, -(10**12)):
            with self.subTest(value=value):
                self.assertEqual(add(value, 0), value)

    def test_commutative(self):
        pairs = [(1, 2), (-5, 5), (0.25, 0.75), (10**9, -(10**9))]
        for a, b in pairs:
            with self.subTest(a=a, b=b):
                self.assertEqual(add(a, b), add(b, a))

    def test_bool_treated_as_int(self):
        # Python 的 True == 1，验证函数未做类型收紧
        self.assertEqual(add(True, 1), 2)


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

    def test_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)

    def test_divisor_one(self):
        for value in (0, 7, -3, 2.5):
            with self.subTest(value=value):
                self.assertEqual(divide(value, 1), value)

    def test_float_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1.0, 0.0)

    def test_inverse_roundtrip(self):
        cases = [(10, 2), (1, 3), (-9, 4), (0.1, 0.2)]
        for a, b in cases:
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(divide(a, b) * b, a, places=12)

    def test_nan_propagates(self):
        self.assertTrue(math.isnan(divide(float("nan"), 1)))

    def test_infinity(self):
        self.assertEqual(divide(float("inf"), 2), float("inf"))
        self.assertEqual(divide(1, float("inf")), 0)


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

    def test_single_char(self):
        for ch in ("a", "Z", "0", "中"):
            with self.subTest(ch=ch):
                self.assertTrue(is_palindrome(ch))

    def test_digits(self):
        self.assertTrue(is_palindrome("12321"))
        self.assertFalse(is_palindrome("12345"))

    def test_chinese_phrase(self):
        self.assertTrue(is_palindrome("上海自来水来自海上"))
        self.assertFalse(is_palindrome("测试仓库"))

    def test_symbols_only(self):
        # 清理后为空串，与空串比较相等 → True
        self.assertTrue(is_palindrome("!!!"))
        self.assertTrue(is_palindrome(" ,.; "))

    def test_whitespace_only(self):
        self.assertTrue(is_palindrome("\t\n  "))

    def test_mixed_case_reverse(self):
        self.assertTrue(is_palindrome("AbBa"))
        self.assertFalse(is_palindrome("AbBc"))


class TestConsistency(unittest.TestCase):
    """跨函数一致性：代数关系应成立。"""

    def test_add_subtract_roundtrip(self):
        cases = [(7, 3), (-2, 8), (0, 0), (10**15, -(10**15))]
        for a, b in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(add(a, b) - b, a)

    def test_divide_multiply_roundtrip(self):
        cases = [(12, 4), (-15, 5), (1, 8)]
        for a, b in cases:
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(divide(a, b) * b, a, places=12)

    def test_add_associative(self):
        cases = [(1, 2, 3), (-1, 0, 1), (0.5, 0.25, 0.125)]
        for a, b, c in cases:
            with self.subTest(a=a, b=b, c=c):
                self.assertAlmostEqual(add(add(a, b), c), add(a, add(b, c)), places=12)


if __name__ == "__main__":
    unittest.main(verbosity=2)
