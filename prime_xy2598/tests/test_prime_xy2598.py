from prime_xy2598 import prime_xy2598
import pytest
from prime import is_prime

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(4) == False
