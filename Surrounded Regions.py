from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def get_island(coord):
            queue = deque()
            queue.append(coord)
            visited = set()
            visited.add(coord)
            res = []
            while queue:
                x,y = queue.popleft()
                res.append((x,y))

                for new_x, new_y in directions:
                    new_x += x
                    new_y += y

                    if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and (new_x,new_y) not in visited and board[new_x][new_y]=='O':
                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))
                    elif new_x < 0 or new_x >= len(board) or new_y < 0 or new_y >= len(board[0]):
                        return
            for x,y in res:
                board[x][y] = 'X'
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    get_island((i,j))
            