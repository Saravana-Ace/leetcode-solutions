from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        visited = set()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))
        layer = 0
        while queue:
            for i in range(len(queue)):
                x,y = queue.popleft()
                mat[x][y] = layer

                directions = [(-1,0),(1,0),(0,-1),(0,1)]
                for (m, n) in directions:
                    new_x = m+x
                    new_y = n+y

                    if 0 <= new_x < len(mat) and 0 <= new_y < len(mat[0]):
                        if (new_x, new_y) not in visited:
                            queue.append((new_x, new_y))
                            visited.add((new_x, new_y))
            layer += 1

        return mat