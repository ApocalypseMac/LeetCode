from math import sqrt
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
    
    def query(self, i, j):
        pi, pj = self.find(i), self.find(j)
        return pi == pj
    
class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        '''
        def prime(n):
            res = []
            for i in range(2, n):
                flag = True
                for j in range(2, int(sqrt(i)) + 1):
                    if i % j == 0:
                        flag = False
                        break
                if flag:
                    res.append(i)
            return res
        '''
        #print(prime(100))
        k = len(queries)
        if threshold == 0:
            return [True] * k
        if threshold > n // 2:
            return [False] * k
        #plist = prime(n)
        uf = UF(n + 1)
        for p in range(threshold + 1, n // 2 + 1):
            if p <= threshold:
                continue
            pm = p
            while pm + p <= n:
                pm += p
                uf.union(p, pm)
        res = []
        for x, y in queries:
            res.append(uf.query(x, y))
        return res
        