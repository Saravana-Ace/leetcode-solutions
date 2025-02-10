import heapq
from collections import defaultdict
class NumberContainers:

    def __init__(self):
        self.index_to_numbers = {}
        self.number_to_indices = defaultdict(list)
        

    def change(self, index: int, number: int) -> None:
        self.index_to_numbers[index] = number
        heapq.heappush(self.number_to_indices[number], index)
        

    def find(self, number: int) -> int:
        if number not in self.number_to_indices: return -1
        
        temp = self.number_to_indices[number]
        while temp:
            index = temp[0]
            if self.index_to_numbers[index] == number:
                return index
            heapq.heappop(temp)
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)