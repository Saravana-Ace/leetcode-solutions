# solution 1 - using prefix sum and odd/even count
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        curr_sum = odd = even = res = 0

        for num in arr:
            curr_sum += num

            if curr_sum % 2:
                res, odd = res + even + 1, odd + 1
            else:
                res, even = res + odd, even + 1
        
        return res % (10**9 + 7)