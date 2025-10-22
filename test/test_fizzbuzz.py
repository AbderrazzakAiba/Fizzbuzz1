
from src.FizzBuzz import fizzbuzz


def test_0_is_fizzbuzz():
    assert fizzbuzz(0)=="fizzbuzz"
def test_1_is_not_fizzbuzz():
    assert fizzbuzz(1)==1
def test_2_is_not_fizzbuzz():
    assert fizzbuzz(2)==2
