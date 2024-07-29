# Standard Library
from typing import NamedTuple

# Third Party Library
import pytest

# First Party Library
from src.hoge import is_prime


class PrimeTestCase(NamedTuple):
    """
    Class representing a test case for prime number checking.

    Args:
        input (int): The input number to check for primality.
        expected (bool): The expected result (True if prime, False otherwise).
    """

    input: int
    expected: bool


@pytest.mark.parametrize(
    PrimeTestCase._fields,
    [
        PrimeTestCase(input=2, expected=True),
        PrimeTestCase(input=3, expected=True),
        PrimeTestCase(input=4, expected=False),
        PrimeTestCase(input=17, expected=True),
        PrimeTestCase(input=19, expected=True),
    ],
)
def test_is_prime(input: int, expected: bool):
    """
    Test the is_prime function with various cases.

    Args:
        input (int): The input number to check for primality.
        expected (bool): The expected result (True if prime, False otherwise).
    """
    assert is_prime(input) == expected
