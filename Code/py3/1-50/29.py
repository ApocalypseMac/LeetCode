class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0: # zero
            return 0
        if dividend == -2 ** 31 and divisor == -1: # overflow
            return 2 ** 31 - 1
        sgn = (dividend > 0) ^ (divisor > 0)
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor
        result = 0
        for i in range(31, -1, -1):
            if (dividend >> i) >= divisor:
                result += 1 << i
                dividend -= divisor << i
        if sgn:
            return -result
        else:
            return result