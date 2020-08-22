class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return '0'
        res = ""
        while n:
            if n >= 1000:
                temp = str(1000 + n % 1000)[1:]
                res = temp + '.' + res
                n //= 1000
            else:
                temp = str(n % 1000)
                res = temp + '.' + res
                n //= 1000
        return res[:-1]