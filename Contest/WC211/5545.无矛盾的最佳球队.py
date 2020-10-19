class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        stat = list(zip(scores, ages))
        stat.sort(key = lambda x: (x[1], x[0]))
        n = len(stat)
        dp = [0] * (n)
        for i in range(n):
            dp[i] = stat[i][0]
        res = dp[0]
        for i in range(1, n):
            for j in range(i):
                if stat[i][0] >= stat[j][0] and dp[i] < dp[j] + stat[i][0]:
                    dp[i] = dp[j] + stat[i][0]
            res = max(res, dp[i])
        return res