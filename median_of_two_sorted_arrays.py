# solution 1 - brute force/naive solution
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = sorted(nums1 + nums2)
        if len(nums1) % 2 == 0:
            return (nums1[(len(nums1)-1)//2] + nums1[(len(nums1)-1)//2 + 1])/2
        else:
            return nums1[(len(nums1)-1)//2]

# solution 2 - using binary search to find first half of sorted array
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A)-1
        total = len(A) + len(B)
        half_len = total//2

        while True:
            mid = (l+r)//2

            A_left = A[mid] if mid >= 0 else float("-inf")
            A_right = A[mid + 1] if mid + 1 < len(A) else float("inf")
            
            mid2 = half_len-mid-2
            B_left = B[mid2] if mid2 >= 0 else float("-inf")
            B_right = B[mid2+1] if mid2 + 1 < len(B) else float("inf")

            if A_left <= B_right and B_left <= A_right:
                if total % 2:
                    return min(A_right, B_right)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                r = mid-1
            else:
                l = mid+1