# solution 1: greedy/brute force
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        check = set(arr)
        res = 0

        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                prev, curr = arr[i], arr[j]
                temp = 2
                nxt = prev+curr

                while nxt in check:
                    temp += 1
                    prev, curr = curr, nxt
                    nxt = prev+curr
                    res = max(res, temp)

        return res