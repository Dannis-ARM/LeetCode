from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])

        # dis to 0
        dis = [[None for _ in range(n)] for _ in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dis[i][j] = 0
                    visited[i][j] = True
                    queue.append((i,j,))

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        depth = 0
        while len(queue) != 0:
            queue_len = len(queue)
            for _ in range(queue_len):
                cur_i, cur_j = queue.popleft()
                if not visited[cur_i][cur_j] and mat[cur_i][cur_j] == 1:
                    dis[cur_i][cur_j] = depth
                visited[cur_i][cur_j] = True

                for dir in dirs:
                    child_i = cur_i + dir[0]
                    child_j = cur_j + dir[1]

                    if child_i >= 0 and child_i < m and child_j >= 0 and child_j < n and not visited[child_i][child_j]:
                        queue.append((child_i, child_j,))
            depth += 1

        return dis
    

from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])

        # dis to 0
        dis = [[None for _ in range(n)] for _ in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dis[i][j] = 0
                    visited[i][j] = True
                    queue.append((i,j,))

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        depth = 0
        while len(queue) != 0:
            queue_len = len(queue)
            for _ in range(queue_len):
                cur_i, cur_j = queue.popleft()
               
                for dir in dirs:
                    child_i = cur_i + dir[0]
                    child_j = cur_j + dir[1]

                    if child_i >= 0 and child_i < m and child_j >= 0 and child_j < n and not visited[child_i][child_j]:
                        visited[child_i][child_j] = True
                        dis[child_i][child_j] = depth + 1
                        queue.append((child_i, child_j,))
            depth += 1

        return dis