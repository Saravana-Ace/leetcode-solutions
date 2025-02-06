from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        num_of_pairs = {}
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                temp = nums[i] * nums[j]
                if temp in num_of_pairs:
                    res += 8 * num_of_pairs[temp]
                    num_of_pairs[temp] += 1
                else:
                    num_of_pairs[temp] = 1
                j += 1

        return res