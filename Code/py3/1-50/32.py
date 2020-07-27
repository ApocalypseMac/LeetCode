class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 2)
        s = '  ' + s # avoid index exceed
        maxval = 0
        for i in range(2, n + 2):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = 2
                    dp[i] += dp[i - 2] # vaild parentheses before curr one
                else:
                    if s[i - 1 - dp[i - 1]] == '(':
                        dp[i] = dp[i - 1] + 2
                        dp[i] += dp[i - 2 - dp[i - 1]] # vaild parentheses before curr one
            maxval = max(maxval, dp[i])
        return maxval
                    
                    