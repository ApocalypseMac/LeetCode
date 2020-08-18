#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = []
        curr = s[0]
        freq = 1
        res = 0
        for ch in s[1:]:
            if ch == curr:
                freq += 1
            else:
                curr = ch
                count.append(freq)
                freq = 1
        count.append(freq)
        for i in range(1, len(count)):
            res += min(count[i], count[i - 1])
        return res
        
# @lc code=end

