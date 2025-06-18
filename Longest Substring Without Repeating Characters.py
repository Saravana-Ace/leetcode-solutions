class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        char_set = set()
        l = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            char_set.add(s[r])
            res = max(res, len(char_set))
        
        return res