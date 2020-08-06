#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # similar with lc41
        n = len(nums)
        nums.append(-1) # avoid exceed
        for i in range(n):
            while nums[i] >= 0 and nums[i] != i:
                # cannot swap directly
                temp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = temp
                
            #print(nums)
        for i in range(n + 1):
            if nums[i] != i:
                return i        


# @lc code=end

