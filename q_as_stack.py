# from collections import deque
class MyQueue:
    def __init__(self):
        self.first = []
        self.second = []

    def push(self, x: int) -> None:
        if not self.second:
            self.second.append(x)
            return
        while self.second:
            self.first.append(self.second.pop())
        self.second.append(x)
        while self.first:
            self.second.append(self.first.pop())

    def pop(self) -> int:
        return self.second.pop()

    def peek(self) -> int:
        return self.second[-1]

    def empty(self) -> bool:
        return not self.second
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()