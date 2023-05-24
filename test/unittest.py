import unittest
from dummy import add_numbers, subtract_numbers, multiply_numbers, divide_numbers
from dummy import concatenate_strings, capitalize_string, reverse_string


class MathFunctionsTestCase(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(8, 4), 4)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(7, 2), 14)

    def test_divide_numbers(self):
        self.assertEqual(divide_numbers(20, 10), 2)
        self.assertEqual(divide_numbers(10, 0), "Division by zero")


class StringFunctionsTestCase(unittest.TestCase):
    def test_concatenate_strings(self):
        self.assertEqual(concatenate_strings("Hello", "World"), "HelloWorld")

    def test_capitalize_string(self):
        self.assertEqual(capitalize_string("hello"), "Hello")

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")


if __name__ == '__main__':
    unittest.main()
