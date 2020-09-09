#
# @lc app=leetcode.cn id=457 lang=python3
#
# [457] 环形数组循环
#

# @lc code=start
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        # if visited, val  = 0
        
        def nextpoint(i):
            return (nums[i] + i) % n
        
        for i in range(n):
            if nums[i] == 0: # visited
                continue
            if nums[i] % n == 0: # self loop
                nums[i] = 0
                continue
            slow, fast = i, nextpoint(i)
            while nums[slow] * nums[fast] > 0 and nums[fast] * nums[nextpoint(fast)] > 0:
                if slow == fast:
                    if nextpoint(slow) == slow: # self loop
                        break
                    else:
                        return True
                slow = nextpoint(slow)
                fast = nextpoint(nextpoint(fast))
            direction = nums[i]
            while nums[i] * direction > 0: # change to visited
                temp = nextpoint(i)
                nums[i] = 0
                i = temp
        return False


        
# @lc code=end

