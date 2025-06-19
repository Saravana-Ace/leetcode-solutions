from collections import defaultdict
class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)

        l = 0
        res = 0
        curr_window_max_c = 0

        for r in range(len(s)):
            char_count[s[r]] += 1
            # window = (r-l+1)
            
            curr_window_max_c = max(curr_window_max_c, char_count[s[r]])
            
            while (r-l+1)-curr_window_max_c > k:
                char_count[s[l]] -= 1
                l += 1          
            
            res = max(res, r-l+1)

        return res        