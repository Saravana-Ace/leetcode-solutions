class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k  # Convert to 0-indexed from left
        
        def quickSelect3Way(left, right):
            if left >= right:
                return nums[left]
            
            # Choose pivot (could be random for better average case)
            pivot = nums[right]
            
            # Three-way partitioning
            # lt: elements < pivot
            # gt: elements > pivot  
            # eq: elements = pivot (between lt and gt)
            lt = left      # boundary of < region
            gt = right     # boundary of > region
            i = left       # current element being examined
            
            while i <= gt:
                if nums[i] < pivot:
                    # Move to < region
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    # Move to > region
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                    # Don't increment i - need to examine swapped element
                else:
                    # nums[i] == pivot, it's in correct region
                    i += 1
            
            # After partitioning:
            # [left...lt-1] < pivot
            # [lt...gt] == pivot  
            # [gt+1...right] > pivot
            
            if k < lt:
                # kth element is in < region
                return quickSelect3Way(left, lt - 1)
            elif k > gt:
                # kth element is in > region
                return quickSelect3Way(gt + 1, right)
            else:
                # kth element is in == region
                return pivot
        
        return quickSelect3Way(0, len(nums) - 1)