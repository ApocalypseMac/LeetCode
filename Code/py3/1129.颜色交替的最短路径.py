#
# @lc app=leetcode.cn id=1129 lang=python3
#
# [1129] 颜色交替的最短路径
#

# @lc code=start
from collections import deque
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        neighbour = [[[] for _ in range(n)], [[] for _ in range(n)]]
        for u, v in red_edges:
            neighbour[0][u].append(v)
        for u, v in blue_edges:
            neighbour[1][u].append(v)

        resred = [[-1, -1] for _ in range(n)] # store minimal ODD/EVEN distance (since may have odd loop)
        resblue = [[-1, -1] for _ in range(n)]
        resred[0][0], resblue[0][0] = 0, 0
        def bfs(color, dist): # color 0: red, 1: blue
            queue = deque([0])
            d = 0
            while queue:
                d += 1
                n = len(queue)
                for _ in range(n):
                    curr = queue.popleft()
                    for succ in neighbour[color][curr]:
                        if dist[succ][0] == -1:
                            dist[succ][0] = d
                            queue.append(succ)
                        elif dist[succ][1] == -1 and (d - dist[succ][0]) & 1:
                            dist[succ][1] = d
                            queue.append(succ)
                color = 1 - color
        
        bfs(0, resred)
        bfs(1, resblue)
        res = []
        for i in range(n):
            if resblue[i][0] == -1 and resred[i][0] == -1:
                res.append(-1)
            elif resblue[i][0] == -1:
                res.append(resred[i][0])
            elif resred[i][0] == -1:
                res.append(resblue[i][0])
            else:
                res.append(min(resred[i][0], resblue[i][0]))
        return res

# @lc code=end

