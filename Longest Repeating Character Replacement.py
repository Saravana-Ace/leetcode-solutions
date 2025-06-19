from collections import defaultdict
class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)

        # def get_window_max(l,r):
        #     c = 0
        #     for i in range(l,r+1):
        #         c = max(c, char_count[s[i]])
        #     return c

        l, r = 0, 0
        res = 0
        curr_window_max_c = 0
        for r in range(len(s)):
            char_count[s[r]] += 1
            window = (r-l+1)
            
            curr_window_max_c = max(curr_window_max_c, char_count[s[r]])
            
            if window-curr_window_max_c <= k:
                res = max(res, window)
                continue

            char_count[s[l]] -= 1
            l += 1

        return res
                