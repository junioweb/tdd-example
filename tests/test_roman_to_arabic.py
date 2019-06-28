import pytest

from src.numerals_converter import RomanToArabic


class TestConverterRomanToArabic:

    @pytest.fixture
    def roman_to_arabic(self):
        return RomanToArabic()

    def test_should_convert_to_arabic_1_when_passed_roman_I(self, roman_to_arabic):
        expected_result = 1
        assert roman_to_arabic.convert('I') == expected_result

    def test_should_convert_to_arabic_5_when_passed_roman_V(self, roman_to_arabic):
        expected_result = 5
        assert roman_to_arabic.convert('V') == expected_result

    def test_should_convert_to_arabic_10_when_passed_roman_X(self, roman_to_arabic):
        expected_result = 10
        assert roman_to_arabic.convert('X') == expected_result

    def test_should_convert_to_arabic_50_when_passed_roman_L(self, roman_to_arabic):
        expected_result = 50
        assert roman_to_arabic.convert('L') == expected_result

    def test_should_convert_to_arabic_100_when_passed_roman_C(self, roman_to_arabic):
        expected_result = 100
        assert roman_to_arabic.convert('C') == expected_result

    def test_should_convert_to_arabic_500_when_passed_roman_D(self, roman_to_arabic):
        expected_result = 500
        assert roman_to_arabic.convert('D') == expected_result

    def test_should_convert_to_arabic_1000_when_passed_roman_M(self, roman_to_arabic):
        expected_result = 1000
        assert roman_to_arabic.convert('M') == expected_result

    def test_should_sum_with_previous_when_the_next_numeral_roman_is_equal_or_less(self, roman_to_arabic):
        expected_result = 67
        assert roman_to_arabic.convert('LXVII') == expected_result
