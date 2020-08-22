from collections import deque 
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        self.res = False
        m, n = len(grid), len(grid[0])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        visited = [[False] * n for _ in range(m)]
        def bfs(i, j, val):
            lay = {}
            queue = deque([(i, j, 0)])
            #print(i, j)
            lay[(i, j)] = 0
            while queue:
                x, y, layer = queue.popleft()
                visited[x][y] = True
                #print(x, y)
                for i in range(4):
                    if 0 <= x + dx[i] < m and 0 <= y + dy[i] < n and grid[x+dx[i]][y+dy[i]] == val:
                        if (x+dx[i],y+dy[i]) in lay:
                            if layer + 1 - lay[(x+dx[i],y+dy[i])] > 2:
                                self.res = True
                                return
                            elif layer + 1 == lay[(x+dx[i],y+dy[i])]:
                                self.res = True
                                return
                            else:
                                continue
                        else:    
                            lay[(x+dx[i],y+dy[i])] = layer + 1
                            queue.append((x+dx[i], y+dy[i], layer + 1))
                #print(queue)
                #print(lay)
            return
                        
        
        for i in range(m):
            for j in range(n):
                if visited[i][j] == False:
                    bfs(i, j, grid[i][j])
                    if self.res:
                        return True
                
        return False
                
                