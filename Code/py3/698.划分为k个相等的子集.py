#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sumval = sum(nums)
        if sumval % k:
            return False
        target = sumval // k
        # backtrack
        '''
        nums.sort()
        if nums[-1] > target:
            return False
        def helper(subsets):
            if nums == []:
                return True
            num = nums.pop()
            for i, subset in enumerate(subsets):
                if subset + num <= target:
                    subsets[i] += num
                    if helper(subsets):
                        return True
                    subsets[i] -= num
                if subset == 0:
                    break
            nums.append(num)
            return False
        return helper([0] * k)
        '''
        # dp
        n = len(nums)
        nums.sort() # increasing
        if nums[-1] > target:
            return False
        dp = [False] * (1 << n)
        dp[0] = True
        subsetsum = [0] * (1 << n)
        for state in range(1 << n):
            if dp[state] is False: # do not need transfer
                continue
            for i, num in enumerate(nums):
                nextstate = state | (1 << i)
                if state != nextstate and dp[nextstate] is False:
                    if num <= target - (subsetsum[state] % target):
                        subsetsum[nextstate] = subsetsum[state] + num
                        dp[nextstate] = True
                    else:
                        break
        return dp[-1]


        
# @lc code=end

