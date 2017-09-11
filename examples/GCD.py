#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = unused-import

# ------
# GCD.py
# ------

"""
https://en.wikipedia.org/wiki/Greatest_common_divisor
"""

from typing import Callable

def gcd1 (m: int, n: int) -> int :
    """
    greatest common divisor
    recursive
    """
    assert (m >= 0) and (n >= 0)
    if m == 0 :
        return n
    return gcd1(n % m, m)

def gcd2 (m: int, n: int) -> int :
    """
    greatest common divisor
    iterative
    """
    assert (m >= 0) and (n >= 0)
    while m != 0 :
        m, n = n % m, m
    return n

def test (gcd: Callable[[int, int], int]) -> None :
    """
    testing greatest common divisor
    """
    assert gcd( 0,  0) == 0
    assert gcd( 0,  1) == 1
    assert gcd( 1,  0) == 1
    assert gcd( 6,  9) == 3
    assert gcd( 9,  6) == 3
    assert gcd(21, 35) == 7
    assert gcd(35, 21) == 7
    assert gcd(35, 22) == 1

if __name__ == "__main__" : #pragma: no cover
    print("GCD.py")
    test(gcd1)
    test(gcd2)
    print("Done.")
