#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#

# @lc code=start
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        # LC424
        n = len(A)
        lo = 0
        freq = 0
        maxfreq = 0
        for hi in range(n):
            if A[hi]:
                freq += 1
                maxfreq = max(maxfreq, freq)
            if hi - lo + 1 > maxfreq + K:
                if A[lo]:
                    freq -= 1
                lo += 1
        return n - lo


        
# @lc code=end

