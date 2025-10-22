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
        (-1,-1),
        (100,"buzz"),
        (45,"fizzbuzz"),
        (7,7),
        (25,"buzz"),
        (21,"fizz"),
        (35,"buzz"),
        (83,83),
        (90,"fizzbuzz"),
        (17,17),
        (75,"fizzbuzz"),
    ]
)
def test_numbers_return_expected(nombre, expected_result):
    actual_result = fizzbuzz(nombre)
    assert actual_result == expected_result



