class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        number_to_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res = []
        def backtrack(temp, digits):
            if not digits:
                res.append("".join(temp[:]))
                return
            letters = number_to_letter[digits[0]]
            for letter in letters:
                temp.append(letter)
                backtrack(temp, digits[1:])
                temp.pop()
        
        backtrack([], digits)
        return res

