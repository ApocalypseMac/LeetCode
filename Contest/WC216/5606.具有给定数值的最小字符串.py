class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        seq = [0] * n
        k -= n
        i = n - 1
        while k:
            if k <= 25:
                seq[i] += k
                k = 0
            else:
                seq[i] += 25
                k -= 25
            i -= 1
        res = ""
        for num in seq:
            res += chr(ord('a') + num)
        return res
        