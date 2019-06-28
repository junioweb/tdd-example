class RomanToArabic:
    def __init__(self):
        self._alias_roman_numeral = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    def convert(self, roman_numeral):
        list_roman_numeral = list(roman_numeral)
        if len(list_roman_numeral) == 1:
            return self._alias_roman_numeral[roman_numeral]
        else:
            previous = 0
            result = 0
            for numeral in list_roman_numeral:
                if not previous:
                    previous = self._alias_roman_numeral[numeral]
                    result = self._alias_roman_numeral[numeral]
                elif self._alias_roman_numeral[numeral] <= previous:
                    result += self._alias_roman_numeral[numeral]
                    previous = self._alias_roman_numeral[numeral]
            return result
