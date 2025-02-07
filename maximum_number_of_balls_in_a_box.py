class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box_map = {}
        for i in range(lowLimit, highLimit+1):
            temp, val = 0, i

            while val != 0:
                temp += val % 10
                val = val // 10
            
            box_map[temp] = (box_map.get(temp, 0) + 1)
        
        return max(box_map.values())