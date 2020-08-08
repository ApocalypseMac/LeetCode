#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        start = 0
        while start + 1 < n and nums[start] == nums[start + 1]:
            start += 1 
        if start == n - 1: # all elements are same
            return 1
        res = 2
        diff = nums[start + 1] - nums[start]
        for i in range(start + 1, n - 1):
            newdiff = nums[i + 1] - nums[i]
            if newdiff * diff >= 0: # same inc/dec or keep
                diff += newdiff
            else: # wiggle
                diff = newdiff
                res += 1
        return res




# @lc code=end

