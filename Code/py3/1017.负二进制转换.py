#
# @lc app=leetcode.cn id=1017 lang=python3
#
# [1017] 负二进制转换
#

# @lc code=start
class Solution:
    def baseNeg2(self, N: int) -> str:
        res = ""
        while N:
            res += str(N & 1)
            N = -(N // 2)
            #print(N)
        if res == "":
            return "0"
        return res[::-1]


        
        
        
# @lc code=end

