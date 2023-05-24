from dummy import add_numbers, subtract_numbers, multiply_numbers, divide_numbers
from dummy import concatenate_strings, capitalize_string, reverse_string


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0


def test_subtract_numbers():
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(10, 10) == 5


def test_multiply_numbers():
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(2, 5) == 8


def test_divide_numbers():
    assert divide_numbers(10, 2) == 5


def test_concatenate_strings():
    assert concatenate_strings("Hello", "World") == "HelloWorld"


def test_capitalize_string():
    assert capitalize_string("hello") == "Hello"


def test_reverse_string():
    assert reverse_string("hehe") == "wrong"
