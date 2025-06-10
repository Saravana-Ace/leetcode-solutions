# use two prefix multiplication arrays
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward, backward = [], []

        forward.append(1)
        temp = 1
        for num in nums:
            temp *= num
            forward.append(temp)

        temp = 1
        for j in range(len(nums)-1, -1, -1):
            temp *= nums[j]
            backward.append(temp)
        
        backward.append(1)

        res = []
        disp = len(backward)-3
        length = len(forward)-1
        
        return [forward[i] * backward[disp-i] for i in range(length)]