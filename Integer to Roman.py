class Solution:
    def intToRoman(self, num: int) -> str:
        # Mapping of integers to roman numerals (descending order)
        mapping = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        result = ""
        
        for value, symbol in mapping:
            # How many times does this value fit?
            count = num // value
            # Add the symbols
            result += symbol * count
            # Update remaining number
            num %= value
        
        return result
