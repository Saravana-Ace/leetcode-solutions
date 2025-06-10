# DFS and BFS Solutions
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(board), len(board[0])
        visited = set()

        def bfs(coord):
            queue = deque([coord])

            while queue:
                x,y = queue.popleft()

                board[x][y] = "T"
                for new_x, new_y in directions:
                    new_x, new_y = new_x + x, new_y + y

                    if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
                        if (new_x,new_y) not in visited and board[new_x][new_y]=='O':
                            queue.append((new_x, new_y))
                            visited.add((new_x, new_y))
        
        # def dfs(coord):
        #     x,y = coord

        #     if x < 0 or x >= rows or y < 0 or y >= cols or board[x][y] != "O" or (x,y) in visited:
        #         return
            
        #     board[x][y] = "T"
        #     visited.add(coord)

        #     for new_x, new_y in directions:
        #         bfs((x+new_x,y+new_y))

        for r in range(rows):
            if board[r][0] == "O": 
                bfs((r,0))
            if board[r][cols-1] == "O": 
                bfs((r,cols-1))
        
        for c in range(cols):
            if board[0][c] == "O": 
                bfs((0,c))
            if board[rows-1][c] == "O": 
                bfs((rows-1,c))
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
            