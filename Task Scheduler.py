from collections import Counter, deque
import heapq
# import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)
        time = 0
        queue = deque()

        while heap or queue:

            if heap:
                count = heapq.heappop(heap)
                count += 1
                if count:
                    queue.append((count, time+n))
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
            
            time += 1

        
        return time