from collections import defaultdict, Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        check = Counter(s1)
        window_char_count = defaultdict(int)
        unique_char_count = 0
        for r in range(len(s2)):
            window_char_count[s2[r]] += 1

            if s2[r] in check and window_char_count[s2[r]] == check[s2[r]]:
                unique_char_count += 1
            
            if unique_char_count == len(check): return True

            if r-l+1 == len(s1):
                if s2[l] in check and window_char_count[s2[l]] == check[s2[l]]:
                    unique_char_count -= 1

                window_char_count[s2[l]] -= 1
                l += 1

        return False
            