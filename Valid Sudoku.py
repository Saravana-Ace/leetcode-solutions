from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = defaultdict(set)
        number_row = defaultdict(set)
        number_col = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".": continue

                if board[i][j] in squares[(i//3,j//3)] or i in number_row[board[i][j]] or j in number_col[board[i][j]]:
                    return False

                squares[(i//3,j//3)].add(board[i][j])
                number_row[board[i][j]].add(i)
                number_col[board[i][j]].add(j)
        return True