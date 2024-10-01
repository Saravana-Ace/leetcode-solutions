# using a set to store the chars that we've already visited
# the char_set also stores the substring, meaning that we 
# can also check with len(char_set)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        i, res = 0, 0

        for j in range(len(s)):
            while s[j] in char_set:
                char_set.remove(s[i])
                i += 1
            
            char_set.add(s[j])
            # res = max(res, j-i+1)
            res = max(res, len(char_set))

        return res