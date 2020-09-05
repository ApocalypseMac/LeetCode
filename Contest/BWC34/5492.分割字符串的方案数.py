class Solution:
    def numWays(self, s: str) -> int:
        n = len(s)
        ones = []
        for i in range(n):
            if s[i] == '1':
                ones.append(i)
        m = len(ones)
        if m % 3 != 0:
            return 0
        elif m == 0:
            return ((n - 1) * (n - 2) // 2) % (10 ** 9 + 7)
        else:
            m1 = m // 3
            x = ones[m1] - ones[m1-1]
            y = ones[m1*2] - ones[m1*2-1]
            return (x * y) % (10 ** 9 + 7)
            
                