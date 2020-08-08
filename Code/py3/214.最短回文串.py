#
# @lc app=leetcode.cn id=214 lang=python3
#
# [214] 最短回文串
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # bruteforce
        s1 = s[::-1]
        n = len(s)
        for i in range(n):
            if s1[i:] == s[:n-i]:
                return s1 + s[n-i:]
        return s1 + s
# @lc code=end

