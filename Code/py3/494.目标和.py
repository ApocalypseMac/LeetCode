#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # dfs(TLE)
        '''
        sumval = sum(nums)
        if sumval < abs(S):
            return 0
        memo = {0: -sumval}
        res = 0
        if S == -sumval:
            res += 1
        nums.sort(reverse=True)
        i = 0
        while nums and nums[-1] == 0:
            nums.pop()
            i += 1
        mul = 1 << i
        n = len(nums)
        def helper(state, currsum, i):
            nonlocal res
            if i == n:
                return
            for flip in range(i, n):
                nextsum = currsum + 2 * nums[flip]
                nextstate = state | (1 << flip)
                if nextsum > S:
                    continue
                elif nextstate in memo:
                    continue
                else:
                    memo[nextstate] = nextsum
                    if nextsum == S:
                        res += 1
                        continue
                    else:
                        helper(nextstate, nextsum, flip + 1)
            return
        
        helper(0, -sumval, 0)
        return res * mul
        '''
        # dp
        sumval = sum(nums)
        if sumval < abs(S):
            return 0
        dp = [0] * (2 * sumval + 1) # [-sumval, sumval]
        dp[0] = 1 # initial: all minus
        dp[2 * nums[0]] += 1
        for num in nums[1:]:
            for i in range(2 * sumval, 2 * num - 1, -1): # 0-1 backpack
                dp[i] += dp[i - 2 * num]
        return dp[sumval + S]


# @lc code=end

