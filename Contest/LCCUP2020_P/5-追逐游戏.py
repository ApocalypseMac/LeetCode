from collections import deque
from copy import deepcopy
class Solution:
    def chaseGame(self, edges: List[List[int]], startA: int, startB: int) -> int:
        n = len(edges)
        isloop = [True] * (n + 1)
        disloop = [-1] * (n + 1)
        disA = [-1] * (n + 1)
        disB = [-1] * (n + 1)
        neighbour = [[] for _ in range(n + 1)]
        degree = [0] * (n + 1)
        for u, v in edges:
            neighbour[u].append(v)
            neighbour[v].append(u)
            degree[u] += 1
            degree[v] += 1
        #print(neighbour, degree)
        
        if n == 3:
            return 1
        elif startB in neighbour[startA]:
            return 1
        
        d1 = degree[:]
        queue = deque([])
        for i in range(1, n + 1):
            if d1[i] == 1:
                queue.append(i)
                isloop[i] = False
                d1[i] -= 1
        while queue:
            curr = queue.popleft()
            for nex in neighbour[curr]:
                if isloop[nex]:
                    d1[nex] -= 1
                    if d1[nex] == 1:
                        isloop[nex] = False
                        queue.append(nex)
        #print(isloop)
                
        # calculate length
        lenloop = 0
        queue1 = deque([])
        for i in range(1, n + 1):
            if isloop[i]:
                lenloop += 1
                queue1.append((i, 0))
                disloop[i] = 0
        #print(lenloop)

        def bfs(queue, disx):
            for v, dis in queue:
                disx[v] = dis
            while queue:
                curr, dis = queue.popleft()
                for nex in neighbour[curr]:
                    if disx[nex] == -1:
                        disx[nex] = dis + 1
                        queue.append((nex, dis + 1))
        
        bfs(queue1, disloop)
        bfs(deque([(startA, 0)]), disA)
        bfs(deque([(startB, 0)]), disB)
        #print(disloop)
        #print(disA, disB) 
        
        res = -1
        for i in range(1, n + 1):
            if disA[i] > disB[i] + 1:
                res = max(res, disA[i])
        #print(res)

        if lenloop == 3:
            return res
        elif isloop[startB] is True: # B in loop
            return -1
        for i in range(1, n + 1):
            if isloop[i] and disA[i] > disB[i] + 1:
                return -1
        return res





        