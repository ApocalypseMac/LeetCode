from heapq import heappush, heappop
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        p = [[0] * (n + 1) for _ in range(m + 1)]
        p1 = [0] * (n + 1)
        res = []
        cnt = 0
        for i in range(m):
            for j in range(n):
                p1[j+1] = p1[j] ^ matrix[i][j]
                p[i+1][j+1] = p[i][j+1] ^ p1[j+1]
                heapq.heappush(res, p[i+1][j+1])
                cnt += 1
                if cnt > k:
                    heapq.heappop(res)
        #print(p)
        #print(res)
        return res[0]
                