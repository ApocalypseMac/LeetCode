#
# @lc app=leetcode.cn id=214 lang=python3
#
# [214] 最短回文串
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # bruteforce
        '''
        s1 = s[::-1]
        n = len(s)
        for i in range(n):
            if s1[i:] == s[:n-i]:
                return s1 + s[n-i:]
        return s1 + s
        '''
        # kmp
        s1 = s + '#' + s[::-1]
        n = len(s1)
        def pmt(s):
            ans = [0] * len(s)
            i, j = 1, 0
            while i < n:
                if s[i] == s[j]:
                    i += 1
                    j += 1
                    ans[i - 1] = j
                elif j == 0:
                    i += 1
                    ans[i - 1] = j
                else:
                    j = ans[j - 1]
            return ans

        m = pmt(s1)[-1]
        return s[::-1] + s[m:]


# @lc code=end

