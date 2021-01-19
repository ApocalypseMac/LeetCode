class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m - 2, -1, -1):
            for j in range(n):
                if matrix[i][j] and matrix[i+1][j]:
                    matrix[i][j] = matrix[i+1][j] + 1
        #print(matrix)
        res = 0
        for row in matrix:
            row.sort(key = lambda x: -x)
            for i in range(n):
                res = max(res, (i + 1) * row[i])
        return res