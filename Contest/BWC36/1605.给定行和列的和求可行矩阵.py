class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if colSum[j] >= rowSum[i]:
                    res[i][j] = rowSum[i]
                    colSum[j] -= rowSum[i]
                    rowSum[i] = 0
                    break
                else:
                    res[i][j] = colSum[j]
                    rowSum[i] -= colSum[j]
                    colSum[j] = 0
        return res