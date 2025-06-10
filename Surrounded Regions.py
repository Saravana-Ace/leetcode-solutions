# BFS Solution right now
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def get_island(coord):
            queue = deque([coord])
            visited = {coord}

            while queue:
                x,y = queue.popleft()

                board[x][y] = "T"
                for new_x, new_y in directions:
                    new_x, new_y = new_x + x, new_y + y

                    if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
                        if (new_x,new_y) not in visited and board[new_x][new_y]=='O':
                            queue.append((new_x, new_y))
                            visited.add((new_x, new_y))

        
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            if board[r][0] == "O": 
                get_island((r,0))
            if board[r][cols-1] == "O": 
                get_island((r,cols-1))
        
        for c in range(cols):
            if board[0][c] == "O": 
                get_island((0,c))
            if board[rows-1][c] == "O": 
                get_island((rows-1,c))
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
            