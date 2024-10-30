class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        mapper = {}
        count = {}
        for num in nums:
            if num not in mapper:
                mapper[num**2] = num
            else:
                if math.sqrt(num) not in count:
                    count[num] = 2
                else:
                    count[num] = count[math.sqrt(num)] + 1
                mapper[num**2] = num
        
        res = -1
        for val in count.values():
            res = max(res, val)
        
        return res