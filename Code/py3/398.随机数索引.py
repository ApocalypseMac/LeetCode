#
# @lc app=leetcode.cn id=398 lang=python3
#
# [398] 随机数索引
#

# @lc code=start
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.length = len(nums)
        

    def pick(self, target: int) -> int:
        count = 0
        res = 0
        for i in range(self.length):
            if self.nums[i] == target:
                count += 1
                if random.random() < 1 / count:
                    res = i
        return res

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end

