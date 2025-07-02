class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 0
        for i, j in groupby(word):
            res += len([*j])-1 
        return res + 1
