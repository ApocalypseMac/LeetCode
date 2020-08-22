class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inv = [0] * n
        for edge in edges:
            inv[edge[1]] += 1
        res = []
        for i in range(n):
            if inv[i] == 0:
                res.append(i)
        return res