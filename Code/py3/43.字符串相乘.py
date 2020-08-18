#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # method1
        '''
        m, n = len(num1), len(num2)
        res = 0
        for i in range(m):
            for j in range(n):
                res += (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0')) * 10 ** (m + n - 2 - i - j)
        return str(res)
        '''
        # method2
        if num1 == '0' or num2 == '0':
            return '0'
        m, n = len(num1), len(num2)
        mul = [0] * (m + n + 2)
        for i in range(m):
            for j in range(n):
                mul[m + n - 2 - i - j] += (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
        for i in range(m + n + 1):
            mul[i], carry = mul[i] % 10, mul[i] // 10
            mul[i + 1] += carry
        res = ""
        zeroflag = True
        for num in mul[::-1]:
            if num:
                res += str(num)
                zeroflag = False
            elif zeroflag:
                continue
            else:
                res += str(num)
        return res
# @lc code=end

