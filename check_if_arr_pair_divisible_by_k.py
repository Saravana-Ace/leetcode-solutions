class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = {}

        for n in arr:
            rem = n%k
            freq[rem] = freq.get(rem, 0) + 1
        
        if 0 in freq and freq[0]%2 == 1: return 0
        
        for i in range(1, k):
            if i in freq and k-i not in freq: return 0
            if i in freq and k-i in freq and freq[i] != freq[k-i]: return 0

        return 1