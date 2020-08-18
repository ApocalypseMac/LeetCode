#
# @lc app=leetcode.cn id=1300 lang=python3
#
# [1300] 转变数组后最接近目标值的数组和
#

# @lc code=start
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        if len(arr) == 1:
            return min(arr[0], target)
        mindiff = 10 ** 9
        minval = -1
        lo, hi = 0, max(arr)
        def diff(val):
            res = 0
            for num in arr:
                if num >= val:
                    res += val
                else:
                    res += num
            return res - target
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            dif = diff(mid)
            if abs(dif) < mindiff:
                mindiff = abs(dif)
                minval = mid
            elif abs(dif) == mindiff and mid < minval:
                minval = mid
            if dif == 0:
                hi = mid - 1
            elif dif > 0:
                hi = mid - 1
            else:
                lo = mid + 1
        return minval

# @lc code=end

