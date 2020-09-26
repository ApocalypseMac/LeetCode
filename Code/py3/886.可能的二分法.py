#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] 可能的二分法
#

# @lc code=start
class Solution:
    from collections import deque
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        edges = [[] for _ in range(N + 1)]
        colors = [0] * (N + 1)
        for pair in dislikes:
            edges[pair[0]].append(pair[1])
            edges[pair[1]].append(pair[0])
        def bfs(start, color):
            queue = deque([start])
            colors[start] = color
            while queue:
                curr = queue.popleft()
                ccolor = colors[curr]
                for succ in edges[curr]:
                    if colors[succ] == 0:
                        colors[succ] = -ccolor
                        queue.append(succ)
                    elif colors[succ] == ccolor:
                        return False
            return True

        for i in range(1, N + 1):
            if colors[i] == 0:
                if bfs(i, 1) is False:
                    return False
        return True


        
# @lc code=end

