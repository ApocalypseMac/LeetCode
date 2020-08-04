class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            temp1 = 1
            temp2 = 2
            for i in range(2, n):
                temp3 = temp1 + temp2
                temp1 = temp2
                temp2 = temp3
            return temp2