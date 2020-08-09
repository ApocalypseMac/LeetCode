class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        if len(cuts) == 1:
            return n
        cuts = [0] + cuts + [n]
        cuts.sort()
        m = len(cuts)
        dp = [[float('INF')] * (m) for _ in range(m)]
        for i in range(m - 1):
            dp[i][i + 1] = 0

        #print(dp)
        for j in range(2, m):
            for i in range(j - 2, -1, -1):
                for k in range(i, j + 1):

                    dp[i][j] = min(dp[i][j], cuts[j] - cuts[i] + dp[k][j] + dp[i][k])


        print(dp)
        return dp[0][-1]
                
        