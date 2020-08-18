#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp (O(n^2))
        '''
        if len(nums) <= 1:
            return len(nums)
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            temp = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    temp = max(temp, dp[j] + 1)   
            dp[i] = temp
        return max(dp)
        '''
        # dp: "sequence" itself (O(nlogn))
        if len(nums) <= 1:
            return len(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = 1
        def bisearch(lo, hi, n): # first i that dp[i] > n
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if dp[mid] < n:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        for num in nums[1:]:
            if num > dp[result - 1]:
                dp[result] = num
                result += 1
            else:
                index = bisearch(0, result, num)
                dp[index] = num
        return result

# @lc code=end

