class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        ret = 0
        for i in range(len(prices)-1):
            res += prices[i+1] - prices[i]
            if res < 0: res = 0
            ret = max(ret, res)
        return ret
            