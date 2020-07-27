class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = (n > 0) - (n < 0)
        n *= sign
        result = 1.
        while n:
            if n % 2 == 1:
                result *= x
                n -= 1
            x *= x
            n /= 2
        if not sign:
            return 1
        elif sign > 0:
            return result
        else: 
            return 1./ result