#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    from collections import deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        lo, hi = 0, 1
        res = []
        queue = deque([(nums[0], 0)])
        def push(queue, hi):
            while queue and nums[hi] > queue[-1][0]:
                queue.pop()
            queue.append((nums[hi], hi))
            
        while hi < k:
            push(queue, hi)
            hi += 1
        res.append(queue[0][0])
        for hi in range(k, n):
            # move hi
            push(queue, hi)
            # move lo
            if queue[0][1] == lo:
                queue.popleft()
            lo += 1
            res.append(queue[0][0])
        return res

        
# @lc code=end

