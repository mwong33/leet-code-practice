class Solution:
    # O(1) space O(n) time where n is the length of the string
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        roman_int = 0
        letter_index = 0
        
        while letter_index < len(s):
            if letter_index != len(s) - 1 and roman_to_int[s[letter_index]] < roman_to_int[s[letter_index + 1]]:
                    roman_int += (roman_to_int[s[letter_index+1]] - roman_to_int[s[letter_index]])
                    letter_index += 2                    
            else:
                roman_int += roman_to_int[s[letter_index]]
                letter_index += 1
        
        return roman_int
