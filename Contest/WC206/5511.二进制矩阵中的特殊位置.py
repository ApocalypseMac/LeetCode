class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rowsum = [0] * m
        colsum = [0] * n
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    rowsum[i] += 1
                    colsum[j] += 1
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] and rowsum[i] == 1 and colsum[j] == 1:
                    res += 1
        return res