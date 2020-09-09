#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # minheap
        '''
        nums = [1]
        heapq.heapify(nums)
        visited = {1} # avoid repeat
        while n:
            n -= 1
            num = heapq.heappop(nums)
            if 2 * num not in visited:
                heapq.heappush(nums, 2 * num)
                visited.add(2 * num)
            if 3 * num not in visited:
                heapq.heappush(nums, 3 * num)
                visited.add(3 * num)
            if 5 * num not in visited:
                heapq.heappush(nums, 5 * num)
                visited.add(5 * num)
        '''
        # dp
        dp = [0] * n
        dp[0] = 1
        i2, i3, i5 = 0, 0, 0
        for i in range(1, n):
            minval = min(2 * dp[i2], 3 * dp[i3], 5 * dp[i5])
            if minval == 2 * dp[i2]:
                i2 += 1
            if minval == 3 * dp[i3]:
                i3 += 1
            if minval == 5 * dp[i5]:
                i5 += 1
            dp[i] = minval
        
        return dp[-1]
# @lc code=end

