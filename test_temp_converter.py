import unittest
from temp_converter import convert_celcius_to_farenheight

class TempConverterTest(unittest.TestCase):
    # test that our function returns the correct output 
    def test_celcius_is_converted_to_farenheit(self):
        """
            F = C * 9/5 + 32
        """

        actual = convert_celcius_to_farenheight(10)
        expected = 50
        self.assertEqual(actual, expected,
                         'celcius should convert to correct farenheight value')    
