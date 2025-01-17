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

# solution 2 - using queue
from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_checker = set()
        res = deque()
        ret = 0
        for c in s:
            while c in res:
                res.popleft()
            
            res.append(c)
            ret = max(ret, len(res))
        
        return ret

#solution 3 - using pure sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        mapper = {}
        res = 0

        for j in range(len(s)):
            if s[j] in mapper and mapper[s[j]] >= i:
                i = mapper[s[j]]+1

            mapper[s[j]] = j
            res = max(res, j-i+1)
        
        return res