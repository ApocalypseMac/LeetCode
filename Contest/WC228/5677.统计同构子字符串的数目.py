class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10 ** 9 + 7
        s += '#'
        res = 0
        ccnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                ccnt += 1
            else:
                res += ccnt * (ccnt + 1) // 2
                ccnt = 1
                res %= mod
            # print(res)
        return res