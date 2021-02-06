from bisect import bisect_left
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort(key = lambda x: x[1])
        starts = [events[_][0] for _ in range(n)]
        ends = [events[_][1] for _ in range(n)]
        # print(events)
        # print(ends)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            s, e, v = events[i - 1]
            l = bisect_left(ends, s)
            # print(i, l)
            for j in range(k, 0, -1):
                dp[i][j] = max(dp[i-1][j], dp[l][j - 1] + v)
        # print(dp)        
        return max(dp[-1])