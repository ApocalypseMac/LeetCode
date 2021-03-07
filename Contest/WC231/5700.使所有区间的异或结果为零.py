class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = [{} for _ in range(k)]
        for i in range(n):
            if nums[i] not in freq[i%k]:
                freq[i%k][nums[i]] = 0
            freq[i%k][nums[i]] += 1
        # print(freq)
        dp = [[0] * 1024 for _ in range(k)]
        max_ = 0
        for i in range(1024):
            if i in freq[0]:
                dp[0][i] = freq[0][i]
                max_ = max(max_, dp[0][i])
        for i in range(1, k):
            # for new in range(1024):
            #     dp[i][new] = dp[i-1][new]
            for j in range(1024):
                tmp = max_
                for k, v in freq[i].items():
                    tmp = max(tmp, dp[i-1][j^k] + v)
                dp[i][j] = tmp
                    
            max_ = max(dp[i])
                    
        return n - dp[-1][0]
                