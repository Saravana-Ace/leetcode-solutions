from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        number_locations = defaultdict(set)
        number_row = defaultdict(set)
        number_col = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j].isnumeric():
                    location = f"{i//3}{j//3}"

                    if board[i][j] in number_locations[location]:
                        return False
                    
                    if i in number_row[board[i][j]] or j in number_col[board[i][j]]:
                        return False

                    number_locations[location].add(board[i][j])
                    number_row[board[i][j]].add(i)
                    number_col[board[i][j]].add(j)
        return True