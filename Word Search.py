class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        def dfs(i, x, y):
            if i == len(word):
                return True
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or word[i] != board[x][y] or (x,y) in visited:
                return

            visited.add((x, y))
            for new_x, new_y in directions:
                if dfs(i+1, new_x+x, new_y+y): return True
            visited.remove((x, y))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(0,i,j): return True

        return False