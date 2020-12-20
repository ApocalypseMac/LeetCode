# Union-Find with path compression and union with rank
class UF:
    def __init__(self, n):
        self.count = [1] * n 
        self.parent = [_ for _ in range(n)]

    def find(self, i): # find root(i) and compress the path
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j): # return if already connected
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            if self.count[pi] < self.count[pj]:
                pi, pj = pj, pi
            self.parent[pj] = pi
            self.count[pi] += self.count[pj]
            return False
        return True
    
    def iscon(self, i, j):
        pi, pj = self.find(i), self.find(j)
        return pi == pj

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        m1, m2 = len(edgeList), len(queries)
        for i in range(m2):
            queries[i].append(i)
        queries.sort(key = lambda x : x[2])
        edgeList.sort(key = lambda x : x[2])
        uf = UF(n)
        i, j = 0, 0
        res = [False] * m2
        for j in range(m2):
            while i < m1 and edgeList[i][2] < queries[j][2]:
                uf.union(edgeList[i][0], edgeList[i][1])
                i += 1
            res[queries[j][3]] = uf.iscon(queries[j][0], queries[j][1])
        return res