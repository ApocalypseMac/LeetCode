#
# @lc app=leetcode.cn id=1526 lang=python3
#
# [1526] 形成目标数组的子数组最少增加次数
#

# @lc code=start
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = 0
        target = [0] + target
        for i in range(len(target) - 1):
            if target[i + 1] > target[i]:
                res += target[i + 1] - target[i]
        return res
            
# @lc code=end

