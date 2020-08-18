#
# @lc app=leetcode.cn id=719 lang=python3
#
# [719] 找出第 k 小的距离对
#

# @lc code=start
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 2:
            return abs(nums[-1] - nums[0])
        nums.sort()
        lo, hi = 0, nums[-1] - nums[0]
        nums.append(float("INF"))
        def count(diff):
            res = 0
            l, r = 0, 0
            while l < n:
                while nums[r] - nums[l] <= diff:
                    r += 1
                res += r - l - 1
                l += 1
            return res

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo

        
# @lc code=end

