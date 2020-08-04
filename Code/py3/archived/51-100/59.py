class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        layer = n // 2
        result = []
        for _ in range(n):
            result.append([0] * n)
        num = 1
        for i in range(layer):
            length = n - 1 - 2 * i
            for j in range(length):
                result[i][i + j] = num
                num += 1
            for j in range(length):
                result[i + j][n - 1 - i] = num
                num += 1
            for j in range(length):
                result[n - 1 - i][n - 1 - i - j] = num
                num += 1
            for j in range(length):
                result[n - 1 - i - j][i] = num
                num += 1
        if n & 1:
            result[layer][layer] = num
        return result