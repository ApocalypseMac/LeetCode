#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        i, j, freq = 1, 1, 1
        while i < n:
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                freq = 1
                i += 1
                j += 1
            else:
                if freq >= 2:
                    freq += 1
                    i += 1
                else:
                    nums[j] = nums[i]
                    freq += 1
                    i += 1
                    j += 1
        return j


# @lc code=end

