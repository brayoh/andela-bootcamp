import unittest
from find_prime import find_prime_number

class TestGetPrimeNumbers(unittest.TestCase):

    def test_returns_correct_output(self):
        result = find_prime_number(11)
        self.assertEquals(result, [2, 3, 5, 7, 11])

    def test_returns_error_if_number_is_zero(self):
        with self.assertRaises(ValueError):
            find_prime_number(0)

    def test_returns_error_if_number_is_negative(self):
        with self.assertRaises(ValueError):
            find_prime_number(-1)

    def test_it_should_accept_integers_only(self):
        with self.assertRaises(TypeError):
            find_prime_number("String")

    def test_it_accepts_whole_numbers_only(self):
        with self.assertRaises(TypeError):
            find_prime_number(1.5)
