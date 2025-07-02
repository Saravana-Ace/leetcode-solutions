class Solution:
    def possibleStringCount(self, word: str) -> int:
        return sum(len([*p])-1 for _,p in groupby(word))+1