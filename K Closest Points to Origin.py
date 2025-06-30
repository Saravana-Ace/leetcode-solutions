import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(-math.sqrt(point[0]**2 + point[1]**2), point) for point in points]
        res = []

        for dist in distances:
            heapq.heappush(res, dist)

        for i in range(len(points)-k):
            heapq.heappop(res)
        res = [point[1] for point in res]
        return res