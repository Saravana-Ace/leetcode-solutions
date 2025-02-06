from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        s_window_count = {}

        for c in set(s):
            s_window_count[c] = 0

        i = 0
        check = 0
        unique_chars = len(set(p))
        res = []

        for j in range(len(s)):
            s_window_count[s[j]] += 1

            if s_window_count[s[j]] == p_count[s[j]]:
                check += 1

            if check == unique_chars:
                while i < len(s) and s[i] not in p_count:
                    i += 1
                
                res.append(i)
            
            if j-i+1 == len(p):
                if s_window_count[s[i]] == p_count[s[i]]:
                    check -= 1
                s_window_count[s[i]] -= 1
                i += 1
        
        return res