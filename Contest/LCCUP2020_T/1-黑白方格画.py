class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
        if k == 0 or k == n * n:
            return 1
        elif k < n:
            return 0
        def comb(x, y): # x < y
            res = 1
            for i in range(x + 1, y + 1):
                res *= i
            for i in range(x + 1, y + 1):
                res //= i - x
            return res
        #print(comb(2, 3))
        #print(comb(2, 5))
        res = 0
        c = 0
        if k % n == 0:
            res += comb(k // n, n)
        while k >= n:
            c += 1
            k -= n
            if k % (n - c) == 0:
                r = k // (n - c)
                #print(r, c)
                res += comb(c, n) * comb(r, n)
        return res
