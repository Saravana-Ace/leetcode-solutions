class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 1
        prev_letter = None
        i = 0
        res = 0
        for i in range(len(word)):
            if word[i] == prev_letter:
                count += 1
            else:
                res += count-1
                count = 1
            prev_letter = word[i]
            
        res += count-1
        return res + 1