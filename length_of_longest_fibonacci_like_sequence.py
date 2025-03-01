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
    
# solution 2: dp
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        check = set(arr)
        dp = [[0] * len(arr) for _ in range(len(arr))]
        res = 0
        mapper = {a:i for i, a in enumerate(arr)}

        for i in reversed(range(len(arr)-1)):
            for j in reversed(range(i+1, len(arr))):
                prev, curr = arr[i], arr[j]
                nxt = prev+curr
                
                dp[i][j] = 2

                if nxt in check:
                    temp = 1 + dp[j][mapper[nxt]]
                    dp[i][j] = temp
                    res = max(res, temp)

        return res