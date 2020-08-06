#
# @lc app=leetcode.cn id=650 lang=python3
#
# [650] 只有两个键的键盘
#

# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
        # prime decomposition
        res = 0
        while n % 2 == 0:
            n //= 2
            res += 2
        while n > 1:
            for i in range(3, 1000, 2):
                if n % i == 0:
                    res += i
                    n //= i
                    break
        return res
        
# @lc code=end

