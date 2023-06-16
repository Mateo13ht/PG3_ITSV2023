import pytest

def roman_to_decimal(roman_number):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    decimal_number = 0
    previous_value = 0

    for char in reversed(roman_number):
        value = roman_values[char]
        if value >= previous_value:
            decimal_number += value
        else:
            decimal_number -= value
        previous_value = value

    return decimal_number

def test_roman_to_decimal():
    assert roman_to_decimal("III") == 3

    assert roman_to_decimal("IV") == 4

    assert roman_to_decimal("IX") == 9

    assert roman_to_decimal("LVIII") == 58

    assert roman_to_decimal("MCMXCIV") == 1994

    assert roman_to_decimal("CD") == 400

    assert roman_to_decimal("MMXIX") == 2019

    assert roman_to_decimal("XC") == 90

    assert roman_to_decimal("MMMCMXCIX") == 3999
