from collections import deque
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [-float('INF')] * n
        dp[0] = nums[0]
        queue = deque([(dp[0], 0)]) # dec
        for i in range(1, n):
            while queue and queue[0][1] + k < i:
                queue.popleft()
            dp[i] = queue[0][0] + nums[i]
            while queue and dp[i] > queue[-1][0]:
                queue.pop()
            queue.append((dp[i], i))
        return dp[-1]