from typing import Tuple


def gcd(a: int, b: int) -> int:
    # Euclidean Algorithm
    # Recursive
    r = a % b
    return b if r == 0 else gcd(b, r)

def gcd_2(a: int, b: int) -> int:
    # Euclidean Algorithm
    # Iterative
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    # Extended Euclidean Algorithm
    # Recursive
    if b == 0:
        # (x, y) = (1, 0)
        return (1, 0, a)
    y, x, d = extended_gcd(b, a % b)
    y -= (a // b) * x
    return x, y, d

