#
# @lc app=leetcode.cn id=330 lang=python3
#
# [330] 按要求补齐数组
#

# @lc code=start
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        hi = 1 # match highest range (not including)
        m = len(nums)
        j = 0 # index of nums
        res = 0
        while hi <= n:
            while j < m and nums[j] <= hi: # '=' must included
                hi += nums[j]
                j += 1
            if hi <= n: # add hi to nums
                #print(hi)
                hi *= 2
                res += 1
        return res
        
# @lc code=end

