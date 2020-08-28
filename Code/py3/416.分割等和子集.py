#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumval = sum(nums)
        n = len(nums)
        if sumval & 1 or n == 1:
            return False
        halfval = sumval >> 1
        # dfs
        '''
        nums.sort(reverse=True)
        if nums[0] > halfval: # simple filter 
            return False
        res = False
        def helper(currsum, index): # currsum, startindex
            nonlocal res
            if res: # find solution
                return
            if currsum == halfval:
                res = True
                return 
            elif currsum > halfval or index == n: # stop recursion
                return
            for i in range(index, n):
                helper(currsum + nums[i], i + 1)
            return
        helper(0, 0)
        return res
        '''
        # dp 2D
        '''
        dp = [[False] * (halfval + 1) for _ in range(n)]
        dp[0][0] = True # initialize
        if nums[0] <= halfval: # put in first one
            dp[0][nums[0]] = True
        for i in range(1, n):
            for j in range(halfval + 1):
                dp[i][j] = dp[i-1][j] # not put in j
                if dp[i][j] is False and nums[i] <= j:
                    dp[i][j] = dp[i - 1][j - nums[i]] # put in j
            if dp[i][halfval]:
                return True
        return False
        '''
        # dp 1D
        dp = [False] * (halfval + 1)
        dp[0] = True
        if nums[0] <= halfval: # put in first one
            dp[nums[0]] = True
        for i in range(1, n):
            for j in range(halfval, -1, -1): # 0-1 backpack: update in REVERSE order
                if nums[i] <= j:
                    dp[j] |= dp[j - nums[i]]
            if dp[-1]:
                return True
        return False
        

                   
        
# @lc code=end

