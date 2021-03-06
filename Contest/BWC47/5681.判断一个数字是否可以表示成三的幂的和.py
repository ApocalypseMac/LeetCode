class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # flag = True
        for i in range(20, -1, -1):
            if n >= 3 ** i:
                n -= 3 ** i
            if n == 0:
                return True
        return False