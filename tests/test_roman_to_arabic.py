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

    def test_should_add_with_previous_when_next_numeral_roman_is_equal_or_less(self, roman_to_arabic):
        expected_result = 67
        assert roman_to_arabic.convert('LXVII') == expected_result

    def test_should_subtract_one_unit_with_next_when_previous_is_equal_I_and_next_is_equal_V_or_X(self, roman_to_arabic):
        expected_result = 9
        assert roman_to_arabic.convert('IX') == expected_result

    def test_should_subtract_ten_units_with_next_when_previous_is_equal_X_and_next_is_equal_L_or_C(self, roman_to_arabic):
        expected_result = 40
        assert roman_to_arabic.convert('XL') == expected_result

    def test_should_subtract_hundred_units_with_next_when_previous_is_equal_C_and_next_is_equal_D_or_M(self, roman_to_arabic):
        expected_result = 900
        assert roman_to_arabic.convert('CM') == expected_result

    def test_should_throw_exception_when_repeat_more_than_three_times_the_same_roman_numeral(self, roman_to_arabic):
        with pytest.raises(ValueError):
            roman_to_arabic.convert('XXXXIIII')

    def test_should_throw_exception_when_repeat_the_roman_numerals_V_L_or_D(self, roman_to_arabic):
        with pytest.raises(ValueError):
            roman_to_arabic.convert('DD')

    def test_should_subtract_with_next_when_between_two_letters_there_is_a_lower(self, roman_to_arabic):
        expected_result = 129
        assert roman_to_arabic.convert('CXXIX') == expected_result
