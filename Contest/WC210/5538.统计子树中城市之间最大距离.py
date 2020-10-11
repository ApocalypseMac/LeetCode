from collections import deque
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        neighbour = [[] for _ in range(n + 1)]
        for x, y in edges:
            neighbour[x].append(y)
            neighbour[y].append(x)
        #print(neighbour)
        distancexy = [[0] * (n + 1) for _ in range(n + 1)]
        def bfs(x, distance, n):
            visited = [False] * (n + 1)
            queue = deque([(x, 0)])
            visited[x] = True
            while queue:
                curr, dis = queue.popleft()
                for n in neighbour[curr]:
                    if visited[n]:
                        continue
                    queue.append((n, dis + 1))
                    visited[n] = True
                    distance[n] = dis + 1
            return
        for i in range(1, n + 1):
            bfs(i, distancexy[i], n)
        #print(distancexy)
        res = [0] * n
        distance = [-1] * (1 << (n + 1))
        def helper(mask, nb, num, clen, n):
            for node in nb:
                if mask & (1 << node):
                    continue
                nmask = mask ^ (1 << node)
                if distance[nmask] != -1:
                    continue
                nnb = nb.copy()
                nnb.remove(node)
                for nx in neighbour[node]:
                    nnb.add(nx)
                nlen = clen
                for i in range(1, n + 1):
                    if nmask & (1 << i):
                        nlen = max(nlen, distancexy[node][i])
                res[nlen] += 1
                distance[nmask] = nlen
                helper(nmask, nnb, num + 1, nlen, n)
            return
        for i in range(1, n + 1):
            helper(1 << i, set(neighbour[i]), 1, 0, n)
        return res[1:]
            
            
            