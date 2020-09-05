class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0
        for i in range(n):
            res += mat[i][i] + mat[i][n-1-i]
        if n % 2 == 1:
            res -= mat[i//2][i//2]
        return res