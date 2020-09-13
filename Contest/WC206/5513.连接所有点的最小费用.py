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

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        n = len(points)
        if n == 1:
            return 0
        if n == 2:
            return distance(points[0], points[1])
        paths = []
        res = 0
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                paths.append((i, j, distance(points[i], points[j])))
        paths.sort(key = lambda x: x[2])
        #print(paths)
        
        uf = UF(n)
        for x, y, distance in paths:
            if uf.union(x, y) is False:
                res += distance
                count += 1
            if count == n - 1:
                break
        return res
        