#
# @lc app=leetcode.cn id=483 lang=python3
#
# [483] 最小好进制
#

# @lc code=start
import math
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n1 = int(n)
        maxdigit = int(math.log2(n1 + 1))
        for digit in range(maxdigit, 1, -1):
            # whether x composed 
            lo, hi = 2, int(math.pow(n1, 1.0 / (digit - 1))) + 1
            print(digit, lo, hi)
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                s = (mid ** digit - 1) // (mid - 1)
                if s == n1:
                    return str(mid)
                elif s > n1:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return str(n1 - 1)
        

        
# @lc code=end

