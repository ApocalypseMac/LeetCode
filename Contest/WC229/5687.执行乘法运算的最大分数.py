class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        res = 0
        n = len(nums)
        m = len(multipliers)
        mul = multipliers
        dp = [[-(10 ** 9)] * (m + 1) for _ in range(m + 1)] # i:left j:right
        dp[0][0] = 0
        for k in range(m): # removed
            for i in range(k + 1):
                j = k - i
                dp[i+1][j] = max(dp[i+1][j], dp[i][j] + mul[k] * nums[i])
                dp[i][j+1] = max(dp[i][j+1], dp[i][j] + mul[k] * nums[n - 1 - j])
        res = - (10 ** 9) 
        for i in range(0, m + 1):
            res = max(res, dp[i][m-i])
        # print(dp)
        return res
            
            