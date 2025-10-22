import pytest
from src.FizzBuzz import fizzbuzz
@pytest.mark.parametrize(
    "nombre, expected_result",
    [
        (0, "fizzbuzz"),
        (1, 1),
        (2,2),
        (15, "fizzbuzz"),
        (30, "fizzbuzz"),

    ]
)
def test_numbers_return_expected(nombre, expected_result):
    actual_result = fizzbuzz(nombre)
    assert actual_result == expected_result
def test_3_is_fizz():
    assert fizzbuzz(3)=="fizz"


