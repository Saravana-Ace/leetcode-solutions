from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""
        t_count = Counter(t)
        have = 0
        need = len(t_count)
        l, r = 0, 0
        res = (float("inf"), -1, -1)

        for r in range(len(s)):
            
            if s[r] in t_count:
                t_count[s[r]] -= 1
                if t_count[s[r]] == 0:
                    have += 1

            while have == need:
                if r-l+1 < res[0]:
                    res = (r-l+1, l, r)

                if s[l] in t_count:
                    t_count[s[l]] += 1
                    if t_count[s[l]] > 0:
                        have -= 1
                l += 1
        
        return s[res[1]:res[2]+1] if res[0] != float("inf") else ""