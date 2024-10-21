class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1: return "0" #base case

        length = (1 << n) - 1
        mid = length//2 + 1

        if k == mid: return "1"

        #if k is less than middle index, then check previous sequence
        if k < mid:
            return self.findKthBit(n-1, k)

        elif k > mid:
            val = self.findKthBit(n-1, length-k+1)
            if val == "1": return "0"
            else: return "1"