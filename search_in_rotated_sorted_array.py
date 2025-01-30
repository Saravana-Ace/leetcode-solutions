class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            # in left portion of array
            if nums[l] <= nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid -1
                # if target > nums[mid] or target < nums[l]:
                #     l = mid + 1
                else:
                    l = mid + 1
            # in right portion of array
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                # if target < nums[mid] or target > nums[r]:
                #     r = mid - 1
                else:
                    r = mid - 1

        return -1