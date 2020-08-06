#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        edges = [[] for _ in range(numCourses)] # out edges
        visited = [False] * numCourses
        for edge in prerequisites:
            indegrees[edge[0]] += 1
            edges[edge[1]].append(edge[0])
        possible = 0
        queue = deque([])
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        while queue:
            curr = queue.popleft()
            visited[curr] = True
            possible += 1
            for succ in edges[curr]:
                if visited[succ] is False:
                    indegrees[succ] -= 1
                    if indegrees[succ] == 0:
                        queue.append(succ)
        return possible == numCourses
                
                


# @lc code=end

