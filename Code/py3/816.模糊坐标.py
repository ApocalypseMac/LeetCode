#
# @lc app=leetcode.cn id=816 lang=python3
#
# [816] 模糊坐标
#

# @lc code=start
class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        S = S[1:-1]
        n = len(S)
        res = []
        def validnum(s): # return list of valid number
            n = len(s)
            if n == 1:
                return [s]
            elif s[0] == '0' and s[-1] == '0':
                return []
            elif s[0] == '0':
                return [s[0] + '.' + s[1:]]
            elif s[-1] == '0':
                return [s]
            else:
                ans = [s]
                for i in range(1, n):
                    ans.append(s[:i] + '.' + s[i:])
            return ans

        for i in range(1, n):
            vl, vr = validnum(S[:i]), validnum(S[i:])
            print(vl, vr)
            if vl and vr:
                for s1 in vl:
                    for s2 in vr:
                        res.append('(' + s1 + ', ' + s2 + ')')
        return res
            


        
# @lc code=end

