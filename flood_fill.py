from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_col = image[sr][sc]
        queue = deque()
        visited = set()
        
        queue.append((sr,sc))
        
        while queue:
            for i in range(len(queue)):
                i, j = queue.pop()
                visited.add((i, j))

                image[i][j] = color
                coords = [(-1,0), (1,0), (0,-1), (0,1)]

                for i_new, j_new in coords:
                    new_i = i+i_new
                    new_j = j+j_new

                    if 0 <= new_i < len(image) and 0 <= new_j < len(image[0]) and (new_i, new_j) not in visited and image[new_i][new_j] == original_col:
                        queue.append((i+i_new, j+j_new))
        
        return image