#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        # math
        '''
        return [i ^ (i >> 1) for i in range(2 ** n)]
        '''
        # iteration
        res = [0]
        for count in range(n):
            for i in range(2 ** count - 1, -1, -1):
                res.append(2 ** count + res[i])
        return res

# @lc code=end

