#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort + greedy O(nlogn)
        if points == []:
            return 0
        n = len(points)
        points.sort(key = lambda x: x[1])
        ans = 1
        arrow = points[0][1]
        for i in range(1, n):
            if points[i][0] > arrow:
                arrow = points[i][1]
                ans += 1
                
        return ans
        
# @lc code=end

