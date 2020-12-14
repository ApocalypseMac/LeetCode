class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        psum = [0]
        p = 0
        for i in range(n):
            p += stones[i]
            psum.append(p)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(psum[j+1] - psum[i+1] - dp[i+1][j], psum[j] - psum[i] - dp[i][j-1])
        #print(dp)
        return dp[0][-1]