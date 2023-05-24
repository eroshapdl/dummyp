import unittest


def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "division by zero"


def concatenate_strings(a, b):
    return a + b


def capitalize_string(string):
    return string.capitalize()


def reverse_string(string):
    return string[::-1]


# unit tests

class MathAndStringFunctionsTestCase(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(8, 4), 4)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(7, 2), 14)

    def test_divide_numbers(self):
        self.assertEqual(divide_numbers(20, 10), 2)
        self.assertEqual(divide_numbers(10, 0), "division by zero")

    def test_concatenate_strings(self):
        self.assertEqual(concatenate_strings("Hello", "World"), "HelloWorld")

    def test_capitalize_string(self):
        self.assertEqual(capitalize_string("hello"), "Hello")

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")


if __name__ == '__main__':
    unittest.main()
