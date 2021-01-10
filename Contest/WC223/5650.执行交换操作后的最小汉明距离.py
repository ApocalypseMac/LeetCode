from sortedcontainers import SortedList
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
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UF(n)
        for u, v in allowedSwaps:
            uf.union(u, v)
        s = dict()
        t = dict()
        
        def dis(a, b):
            res = 0
            for k in a:
                if k in b:
                    b.remove(k)
                else:
                    res += 1
            return res + len(b)
        
        root = [uf.find(i) for i in range(n)]
        for i in range(n):
            if root[i] not in s:
                s[root[i]] = SortedList()
                t[root[i]] = SortedList()
            s[root[i]].add(source[i])
            t[root[i]].add(target[i])
        #print(s, t)   
        res = 0
        for k in s.keys():
            res += dis(s[k], t[k]) // 2
        return res
            
        