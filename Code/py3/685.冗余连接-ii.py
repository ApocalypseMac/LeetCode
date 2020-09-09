#
# @lc app=leetcode.cn id=685 lang=python3
#
# [685] 冗余连接 II
#

# @lc code=start
class UF:
    def __init__(self, n):
        self.count = [1] * n
        self.parent = [_ for _ in range(n)]

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j): # return if already connected
        pi, pj = self.find(i), self.find(j)
        #print(pi, pj)
        if pi != pj:
            if self.count[pi] < self.count[pj]:
                pi, pj = pj, pi
            self.parent[pj] = pi
            self.count[pi] += self.count[pj]
            return False
        return True

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UF(n + 1)
        indegrees = [[] for _ in range(n + 1)]
        flag = False
        for i in range(n):
            if indegrees[edges[i][1]]:
                indegrees[edges[i][1]].append(edges[i][0])
                flag = True
                break
            indegrees[edges[i][1]].append(edges[i][0])
        #istree = True
        if flag:
            for edge in edges[:i] + edges[i+1:]:
                if uf.union(edge[0], edge[1]):
                    #istree = False
                    return [indegrees[edges[i][1]][0], edges[i][1]]
            return edges[i]
        else:
            for edge in edges:
                if uf.union(edge[0], edge[1]):
                    return edge

        
# @lc code=end

