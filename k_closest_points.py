import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        ret = []
        
        for coord in points:
            heapq.heappush(res, (math.sqrt(coord[0]**2 + coord[1]**2), coord))

        for j in range(k):
            ret.append(heapq.heappop(res)[1])
        
        return ret