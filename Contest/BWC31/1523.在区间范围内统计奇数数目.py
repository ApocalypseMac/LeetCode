#
# @lc app=leetcode.cn id=1523 lang=python3
#
# [1523] 在区间范围内统计奇数数目
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        if diff & 1:
            return diff // 2 + 1
        else:
            if high & 1:
                return diff // 2 + 1
            else:
                return diff // 2
# @lc code=end

