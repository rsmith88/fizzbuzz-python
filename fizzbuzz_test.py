from fizzbuzz import Fizzbuzz

def test_fizzbuzz_divisible_by_three():
    result = Fizzbuzz.fizzbuzz(3)
    assert result == 'Fizz'

def test_fizzbuzz_divisible_by_five():
    result = Fizzbuzz.fizzbuzz(5)
    assert result == 'Buzz'

def test_fizzbuzz_divisible_by_fifteen():
    result = Fizzbuzz.fizzbuzz(15)
    assert result == 'FizzBuzz'

def test_fizzbuzz_other():
    result = Fizzbuzz.fizzbuzz(2)
    assert result == str(2)
