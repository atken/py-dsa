import euclidean
import math


def test_gcd():
    assert euclidean.gcd(10, 5) == math.gcd(10, 5)
    assert euclidean.gcd(5, 3) == math.gcd(5, 3)
    assert euclidean.gcd(149210, 4860) == math.gcd(149210, 4860)

def test_gcd_2():
    assert euclidean.gcd_2(10, 5) == math.gcd(10, 5)
    assert euclidean.gcd_2(5, 3) == math.gcd(5, 3)
    assert euclidean.gcd_2(149210, 4860) == math.gcd(149210, 4860)

def test_extended_gcd():
    # 48*1+32*(-1)=16
    assert euclidean.extended_gcd(48, 32) == (1, -1, 16)
    # 172*(-5)+48*18=4
    assert euclidean.extended_gcd(172, 48) == (-5, 18, 4)

