class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m, n = len(words), len(words[0])
        n1 = len(target)
        if n1 > n:
            return 0
        mod = 10 ** 9 + 7
        dp = [[0] * (n + 1) for _ in range(n1 + 1)]
        count = [[0] * 26 for _ in range(n)]
        for wd in words:
            for i in range(n):
                count[i][ord(wd[i]) - ord('a')] += 1
        for i in range(n + 1):
            dp[0][i] = 1
        for i in range(1, n1 + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1] * count[j-1][ord(target[i-1]) - ord('a')]
                dp[i][j] %= mod
        #res = 0
        #print(dp)
        #for i in range(n + 1):
        
        #res += dp[-1][-1]
        #    res %= mod
        return dp[-1][-1] % mod