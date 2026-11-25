"""测试仓库示例模块：供单元测试验证用，不含业务依赖。"""

from __future__ import annotations


def add(a: float, b: float) -> float:
    """返回两数之和。"""
    return a + b


def divide(a: float, b: float) -> float:
    """返回 a / b，除数为 0 时抛 ZeroDivisionError。"""
    if b == 0:
        raise ZeroDivisionError("divisor must not be zero")
    return a / b


def is_palindrome(text: str) -> bool:
    """忽略大小写与非字母数字字符后，判断是否为回文。"""
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print("add(2, 3) =", add(2, 3))
    print("divide(10, 4) =", divide(10, 4))
    print(
        "is_palindrome('A man, a plan, a canal: Panama') =",
        is_palindrome("A man, a plan, a canal: Panama"),
    )
