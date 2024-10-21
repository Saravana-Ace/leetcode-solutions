from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        queue = deque()
        queue.append(amount)
        checker = set()
        checker.add(amount)
        res = 0

        while queue:
            for _ in range(len(queue)):
                curr_amt = queue.popleft()

                if curr_amt == 0: return res
                elif curr_amt < 0: continue

                for c in coins:
                    temp = curr_amt-c
                    if temp not in checker:
                        queue.append(curr_amt-c)
                        checker.add(curr_amt-c)
                    
            res += 1
        
        return -1