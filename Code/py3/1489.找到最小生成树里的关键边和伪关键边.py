#
# @lc app=leetcode.cn id=1489 lang=python3
#
# [1489] 找到最小生成树里的关键边和伪关键边
#

# @lc code=start
class UF:
    def __init__(self, n):
        self.parents = [_ for _ in range(n)]
        self.count = [1] * n
    
    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            if self.count[pi] < self.count[pj]:
                pi, pj = pj, pi
            self.count[pi] += self.count[pj]
            self.parents[pj] = pi
            return True
        return False # if already connected


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        m = len(edges)
        for i in range(m):
            edges[i].append(i)
        
        sedges = sorted(edges, key = lambda x: x[2])
        keyedges = set()
        pkeyedges = set()

        def mst(n, add = -1, delete = -1): # Kruskal
            nonlocal sedges, edges
            uf = UF(n + 1)
            cost = 0
            count = 0
            if add != -1:
                i, j = edges[add][0], edges[add][1]
                cost += edges[add][2]
                count += 1
                uf.union(i, j)
            for edge in sedges:
                if edge[3] != delete:
                    i, j = edge[0], edge[1]
                    if uf.union(i, j):
                        count += 1
                        cost += edge[2]
                    if count == n - 1:
                        return cost
            return -1 # cannot
        
        baseline = mst(n)
        for i in range(m): # force delete edge i
            newval = mst(n, -1, i)
            if newval == -1 or newval > baseline: # not connected or mst cost increase
                keyedges.add(i)
        
        for i in range(m): # force add edge i
            newval = mst(n, i)
            if newval == baseline and i not in keyedges: # can in mst and not necessary
                pkeyedges.add(i)
        

        return [list(keyedges), list(pkeyedges)]

                    
# @lc code=end

