import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]
        temp = []
        for stone in stones:
            heapq.heappush(temp,-stone)

        while len(temp) > 1:
            s1 = -heapq.heappop(temp)
            s2 = -heapq.heappop(temp)
            if s1 != s2:
                heapq.heappush(temp, -abs(s1-s2))
        
        return -temp[0] if temp else 0