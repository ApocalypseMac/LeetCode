#
# @lc app=leetcode.cn id=684 lang=python3
#
# [684] 冗余连接
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UF(n + 1)
        for edge in edges:
            if uf.union(edge[0], edge[1]):
                return edge

        
# @lc code=end

