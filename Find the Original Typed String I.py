class Solution:
    def possibleStringCount(self, word: str) -> int:
        temp = 1
        res = 0

        prev = word[0]
        for i in range(1, len(word)):
            if word[i] == prev:
                temp += 1
            else:
                res += (temp-1) if temp > 0 else 0
                temp = 1
            prev = word[i]
        res = res + (temp-1) if temp > 0 else 0
        return res + 1