class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        neg_flag = False
        if x < 0:
            x = -x
            neg_flag = True
        while x:
            x, temp = x // 10, x % 10
            if neg_flag:
                if result > 214748364 or (result == 214748364 and temp > 8):
                    return 0
            else:
                if result > 214748364 or (result == 214748364 and temp > 7):
                    return 0
            result *= 10
            result += temp
        if neg_flag:
            return -result
        else:
            return result