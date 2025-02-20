class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        check_len = len(nums[0])
        check_nums = set(nums)

        def backtrack(num_str):
            if len(num_str) == check_len and num_str not in check_nums:
                return num_str
            elif len(num_str) == check_len and num_str in check_nums:
                return

            
            temp = backtrack(num_str+"1")
            return temp if temp != None else backtrack(num_str+"0")
        
        return backtrack("")