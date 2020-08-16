#
# @lc app=leetcode.cn id=5185 lang=python3
#
# [5185] 存在连续三个奇数的数组
#

# @lc code=start
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        odda, oddb, oddc = arr[0] & 1, arr[1] & 1, arr[2] & 1
        if odda and oddb and oddc:
            return True
        for i in range(3, len(arr)):
            temp = arr[i] & 1
            odda, oddb, oddc = oddb, oddc, temp
            if odda and oddb and oddc:
                return True
        return False
            
# @lc code=end

