#
# @lc app=leetcode.cn id=1536 lang=python3
#
# [1536] 排布二进制网格的最少交换次数
#

# @lc code=start
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeros = []  # (numzero, numrow)
        for i in range(n):
            nzero = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    nzero += 1
                else:
                    break
            zeros.append(nzero)
        requirement = list(range(n - 1, -1, -1))
        szeros = sorted(zeros)[::-1]
        for i in range(n):
            if requirement[i] > szeros[i]: # check if possible
                return -1
        nstep = 0
        #print(zeros)
        # greedily choose the nearest satisfied one
        for i in range(n - 1):
            for j in range(len(zeros)):
                if zeros[j] >= n - 1 - i:
                    nstep += j
                    zeros.pop(j)
                    break
        return nstep
# @lc code=end

