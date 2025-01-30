class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if nums[r] >= nums[l]:
                return nums[l]
            elif nums[mid] >= nums[l]:#don't need all values to left of mid
                l = mid + 1
            elif nums[mid] < nums[l]: #don't need all values to right of mid
                r = mid