class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n <= 1:
            return
        if n % 2 == 0:
            n1, n2 = n // 2, n // 2
        else:
            n1, n2 = (n + 1) // 2, n // 2
        for i in range(n1):
            for j in range(n2):
                '''
                matrix[i][j], matrix[j][n - 1 - i] = matrix[j][n - 1 - i], matrix[i][j]   
                matrix[i][j], matrix[n - 1 - i][n - 1 - j] = matrix[n - 1 - i][n - 1 - j], matrix[i][j]   
                matrix[i][j], matrix[n - 1 - j][i] = matrix[n - 1 - j][i], matrix[i][j]
                '''
                matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i], matrix[i][j] = matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i]