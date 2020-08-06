#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return 0
        def pmt(s):
            n = len(s)
            ans = [0] * n
            i, j = 1, 0
            while i < n:
                if s[i] == s[j]: # matched
                    j += 1
                    i += 1
                    ans[i - 1] = j
                elif j == 0: # not match, j == 0
                    i += 1
                    ans[i - 1] = j
                else: # not match, general
                    j = ans[j - 1]
            return ans

        ans = pmt(needle) # pmt
        i, j = 0, 0
        while i < n:
            if haystack[i] == needle[j]: # matched
                j += 1
                i += 1
            elif j == 0: # not match, j == 0
                i += 1
            else: # not match, general
                j = ans[j - 1]
            if j == m:
                return i - j
        return -1
# @lc code=end

