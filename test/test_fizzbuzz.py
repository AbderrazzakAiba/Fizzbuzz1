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
        (3, "fizz"),
        (6, "fizz"),
        (5, "buzz"),
        (10, "buzz"),

    ]
)
def test_numbers_return_expected(nombre, expected_result):
    actual_result = fizzbuzz(nombre)
    assert actual_result == expected_result



