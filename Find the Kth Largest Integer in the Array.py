class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(num) for num in nums]
        k = len(nums)-k

        def three_way_partition(left, right):
            i = left
            l_bound = left
            r_bound = right
            pivot = nums[right]

            while i <= r_bound:
                if nums[i] < pivot:
                    nums[l_bound], nums[i] = nums[i], nums[l_bound]
                    l_bound, i = l_bound + 1, i + 1
                elif nums[i] > pivot:
                    nums[i], nums[r_bound] = nums[r_bound], nums[i]
                    r_bound -= 1
                else:
                    i += 1
            
            if k < l_bound:
                return three_way_partition(left, l_bound-1)
            elif k > r_bound:
                return three_way_partition(r_bound+1, right)
            else:
                return str(nums[k])
        
        return three_way_partition(0, len(nums)-1)