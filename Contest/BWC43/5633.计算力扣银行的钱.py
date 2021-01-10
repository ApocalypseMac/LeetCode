class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        for i in range(n):
            res += (i // 7) + i % 7 + 1
        return res