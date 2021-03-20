class Solution:
    @lru_cache(None)
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        gcdval = [[gcd(nums[i], nums[j]) for i in range(n)] for j in range(n)]
        # print(gcdval)
        ns = (1 << n)
        dp0 = []
        for i in range(n):
            for j in range(i + 1, n):
                dp0.append(((1 << i) + (1 << j), gcdval[i][j]))
        dp = [[-1] * ns for _ in range(n // 2 + 1)]
        dp[0][-1] = 0
        for i in range(n // 2):
            for j in range(ns):
                if dp[i][j] != -1:
                    for mask, val in dp0:
                        if mask & j != mask:
                            continue
                        tmp = val * (i + 1)
                        if dp[i+1][j-mask] == -1:
                            dp[i+1][j-mask] = tmp + dp[i][j]
                        else:
                            dp[i+1][j-mask] = max(dp[i+1][j-mask], tmp + dp[i][j])
        return dp[-1][0]
                
            
            
        
        
        
        
        