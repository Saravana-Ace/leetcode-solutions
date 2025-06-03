class Solution:
    def intToRoman(self, num: int) -> str:
        # Define value-symbol pairs in descending order
        # Include subtractive cases (4, 9, 40, 90, 400, 900)
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        result = ""
        
        # Iterate through each value-symbol pair
        for i in range(len(values)):
            # Calculate how many times current value fits into num
            count = num // values[i]
            
            # Add the corresponding symbols to result
            result += symbols[i] * count
            
            # Reduce num by the value we just processed
            num %= values[i]
        
        return result