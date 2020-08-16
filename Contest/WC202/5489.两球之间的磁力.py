#
# @lc app=leetcode.cn id=5489 lang=python3
#
# [5489] 两球之间的磁力
#

# @lc code=start
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        distance = position[-1] - position[0]
        if m == 2:
            return distance
        interval = [position[i] - position[i - 1] for i in range(1, n)]
        maxinterval = distance // (m - 1)
        lo, hi = 0, maxinterval
        #print(lo, hi)
        
        def possible(interval, val):
            i = 0
            temp = 0
            num = 0
            while i < len(interval):
                temp += interval[i]
                if temp >= val:
                    num += 1
                    if num == m - 1:
                        return True
                    temp = 0
                i += 1
            return False
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if possible(interval, mid):
                lo = mid + 1
            else:
                hi = mid - 1
        return lo - 1
       
# @lc code=end

