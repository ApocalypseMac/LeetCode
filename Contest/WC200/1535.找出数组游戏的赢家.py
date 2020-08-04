#
# @lc app=leetcode.cn id=1535 lang=python3
#
# [1535] 找出数组游戏的赢家
#

# @lc code=start
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        m = max(arr)
        indexm = arr.index(m)
        if k >= indexm:
            return m
        arr = arr[:indexm]
        i = 1
        res = arr[0]
        count = 0
        while i < indexm:
            if arr[i] > res:
                count = 1
                res = arr[i]
            else:
                count += 1
            if count == k:
                return res
            i += 1
        return m 
# @lc code=end

