class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            for i in range(len(digits)-1, -1, -1):
                temp = digits[i] + 1
                if temp == 10:
                    digits[i] = 0
                else:
                    digits[i] = temp 
                    break
            if digits[0] == 0:
                digits.insert(0,1)
        else:
            digits[-1] += 1
        
        return digits