#
# @lc app=leetcode.cn id=765 lang=python3
#
# [765] 情侣牵手
#

# @lc code=start
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2
        pos = [-1 for _ in range(2 * n)]
        for i in range(2 * n):
            pos[row[i]] = i
        res = 0
        for i in range(n):
            if row[2*i] // 2 == row[2*i+1] // 2: # this pair of seats has exactly a couple
                continue
            else:
                p1 = row[2*i]
                p2 = (p1 // 2) * 4 + 1 - p1 # p1 and p2 are couple
                p3 = row[2*i+1]
                # swap p2 and p3
                row[2*i+1], row[pos[p2]] = row[pos[p2]], row[2*i+1]
                pos[p2], pos[p3] = pos[p3], pos[p2]
                res += 1
        #print(row)
        return res

        
# @lc code=end

