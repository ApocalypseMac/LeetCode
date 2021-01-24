# Union-Find with path compression and union with rank
class UF:
    def __init__(self, n):
        self.count = [1] * n 
        self.parent = [_ for _ in range(n)]

    def find(self, i): # find root(i) and compress the path
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j): # return True if already connected
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            if self.count[pi] < self.count[pj]:
                pi, pj = pj, pi
            self.parent[pj] = pi
            self.count[pi] += self.count[pj]
            return False
        return True
