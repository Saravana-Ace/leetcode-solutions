from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        number_locations = defaultdict(set)
        number_row = defaultdict(set)
        number_col = defaultdict(set)

        outer = [(0,2), (3,5), (6,8)]
        inner = [(0,2), (3,5), (6,8)]
        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j].isnumeric():
                    # check if in mini grid
                    counter = 1
                    for a,b in outer:
                        for x,y in inner:
                            if a <= i <= b and x <= j <= y:
                                if board[i][j] in number_locations[counter]: 
                                    return False
                                number_locations[counter].add(board[i][j])
                            counter += 1
                
                    if i in number_row[board[i][j]] or j in number_col[board[i][j]]:
                        return False

                    number_row[board[i][j]].add(i)
                    number_col[board[i][j]].add(j)
        return True