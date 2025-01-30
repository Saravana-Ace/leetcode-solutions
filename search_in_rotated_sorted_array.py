class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we only want to do binary search on a 
        # sorted portion, so we need to first check
        # for a valid portion of the array
        
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            # left sorted portion of array
            if nums[l] <= nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1
            # right sorted portion of array
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1