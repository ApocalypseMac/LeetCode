class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp O(n) space
        '''
        if len(nums) == 1:
            return 0 
        dp = [0] * len(nums)
        currmax = 0
        for i in range(len(nums)):
            if i + nums[i] > currmax:
                count = dp[i] + 1
                if i + nums[i] >= len(nums) - 1:
                    return count
                for j in range(currmax + 1, i + nums[i] + 1):
                    dp[j] = count
                currmax = i + nums[i]
        return dp[-1]
        '''
        # Greedy O(1) space
        step = 0
        currmax = 0
        stepmax = 0
        for i in range(len(nums) - 1):
            currmax = max(currmax, i + nums[i])
            if i == stepmax:
                step += 1
                stepmax = currmax
        return step