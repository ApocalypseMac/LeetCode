#
# @lc app=leetcode.cn id=1007 lang=python3
#
# [1007] 行相等的最少多米诺旋转
#

# @lc code=start
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        possible = [True] * 6
        counta = [0] * 6
        countb = [0] * 6
        for i in range(n):
            counta[A[i] - 1] += 1
            countb[B[i] - 1] += 1
            for j in range(6):
                if j == A[i] - 1 or j == B[i] - 1:
                    continue
                else:
                    possible[j] = False
            if any(possible):
                continue
            else:
                return -1
        res = n
        for i in range(6):
            if possible[i]:
                res = min(res, n - counta[i], n - countb[i])
        return res
                
        
# @lc code=end

