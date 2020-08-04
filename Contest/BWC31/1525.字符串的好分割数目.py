#
# @lc app=leetcode.cn id=1525 lang=python3
#
# [1525] 字符串的好分割数目
#

# @lc code=start
class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        l = []
        r = []
        setl = set()
        setr = set()
        res = 0
        for i in range(n - 1):
            setl.add(s[i])
            l.append(len(setl))
        for i in range(n - 1, 0, -1):
            setr.add(s[i])
            if len(setr) == l[i - 1]:
                res += 1
            #print(res)

        return res
# @lc code=end

