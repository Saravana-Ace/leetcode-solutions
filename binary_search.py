class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        
        while j >= i:
            mid = (i+j)//2

            if target > nums[mid]:
                i = mid+1
            elif target < nums[mid]:
                j = mid-1
            elif target == nums[mid]:
                return mid
        
        return -1