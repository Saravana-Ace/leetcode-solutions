class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        def dfs(curr_string, location):
            x,y = location
            curr_string += board[x][y]
            
            if curr_string == word:
                return True
            if curr_string != word[0:len(curr_string)]:
                return

            for new_x, new_y in directions:
                new_x += x
                new_y += y

                if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    if dfs(curr_string, (new_x, new_y)): return True
                    visited.remove((new_x, new_y))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited.add((i,j))
                    if dfs("", (i,j)): return True
                    visited.remove((i,j))

        return False