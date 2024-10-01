class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()

        for k, val in enumerate(nums):
            if k > 0 and val == nums[k-1]:
                continue
            if val > 0:
                break
            i, j = k+1, len(nums)-1
            
            while i < j:
                total = nums[k] + nums[i] + nums[j]
                if total < 0:
                    i += 1
                elif total > 0:
                    j -= 1
                else:
                    res.add(tuple(sorted((nums[k], nums[i], nums[j]))))
                    i+=1
                    while nums[i] == nums[i-1] and i < j:
                        i += 1
                    j-=1
        return res