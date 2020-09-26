#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n + 2) # max height
        res = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[j + 1] += 1
                else:
                    dp[j + 1] = 0
            #print(dp)
            stack = []
            for k in range(n + 2):
                # LC84 for each row
                while stack and dp[k] < stack[-1][0]:
                    h, index = stack.pop()
                    # consider 1,2,5,6,3 with incoming 2
                    # in fact width = k - (stack[-1][1] + 1)
                    w = k - 1 - stack[-1][1] 
                    res = max(res, h * w) 
                stack.append((dp[k], k))
            #print(res)
        return res


            

# @lc code=end

