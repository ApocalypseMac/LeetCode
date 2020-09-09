#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        freq = 0
        maxfreq = 0
        for num in nums:
            if num:
                freq += 1
                maxfreq = max(maxfreq, freq)
            else:
                freq = 0
        return maxfreq
        
# @lc code=end

