#
# @lc app=leetcode.cn id=5488 lang=python3
#
# [5488] 使数组中所有元素相等的最小操作数
#

# @lc code=start
class Solution:
    def minOperations(self, n: int) -> int:
        # average: n
        if n & 1:
            n //= 2
            return n * (n + 1)
        else:
            n //= 2
            return n ** 2
# @lc code=end

