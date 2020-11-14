from collections import deque
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        if x == 0:
            return 0
        visited = [[False] * 8001 for _ in range(2)] 
        # 4001 will not enough (maybe 6001)
        # consider jump forward twice from boundary (~2000)
        for i in forbidden:
            visited[0][i] = True
            visited[1][i] = True
        if visited[0][x] is True:
            return -1
        #print(visited)
        # (site, state)
        # state 0: forward 1: backward
        queue = deque([(0, 0, 0)])
        while queue:
            site, state, n = queue.popleft()
            if state == 0:
                ns = site - b
                if ns == x:
                    return n + 1
                if ns >= 0 and visited[1][ns] is False:
                    visited[1][ns] = True
                    queue.append((ns, 1, n + 1))
            ns1 = site + a
            if ns1 == x:
                return n + 1
            if ns1 < 8001 and visited[0][ns1] is False:
                visited[0][ns1] = True
                queue.append((ns1, 0, n + 1))
        return -1