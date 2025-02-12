class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def num_sum(num):
            res = 0
            while num != 0:
                res += num%10
                num //= 10
            return res
        
        sums = []
        sums_mapper = {}
        for i in range(len(nums)):
            val = num_sum(nums[i])
            sums.append(val)
            if val not in sums_mapper:
                sums_mapper[val] = [nums[i], i]
            else:
                if nums[i] > sums_mapper[val][0]:
                    sums_mapper[val][0] = nums[i]
                    sums_mapper[val][1] = i
        
        res = -1
        for j in range(len(sums)):
            if sums[j] in sums_mapper and j != sums_mapper[sums[j]][1]:
                res = max(res, nums[j] + sums_mapper[sums[j]][0])

        return res