#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash table
        dict = {}
        for i, n in enumerate(nums):
            if target - n in dict:
                return [dict[target-n], i]
            dict[n] = i
        return -1
        
# @lc code=end

