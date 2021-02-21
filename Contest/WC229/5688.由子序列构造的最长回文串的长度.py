class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        word2 = word2[::-1]
        m, n = len(word1), len(word2)
        lcs = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    lcs[i][j] = lcs[i - 1][j - 1] + 1
                else:
                    lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])
    
        def pal(s, n):
            n = len(s)
            dp = [[1] * n for _ in range(n)]
            # for i in range(n):
            #     dp[i][i] = 1
            for i in range(n - 1):
                if s[i] == s[i+1]:
                    dp[i][i+1] = 2
            for k in range(2, n):
                for i in range(n - k):
                    if s[i] == s[i+k]:
                        tmp = dp[i+1][i+k-1] + 2
                    else:
                        tmp = max(dp[i+1][i+k], dp[i][i+k-1])
                    dp[i][i+k] = tmp
            return [dp[_][-1] for _ in range(n)] + [0]
        
        pa1 = pal(word1, m)
        pa2 = pal(word2, n)
        # print(lcs)
        # print(pa1, pa2)
        res = 0
        for i in range(m):
            for j in range(n):
                if lcs[i+1][j+1] > 0:
                    res = max(res, 2 * lcs[i+1][j+1] + max(pa1[i+1], pa2[j+1]))
        return res