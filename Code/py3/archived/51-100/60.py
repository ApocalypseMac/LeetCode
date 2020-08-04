class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1 # start from 0
        mod = [1] # factorial ([n - 1, 0])
        f = 1
        for i in range(1, n):
            f *= i
            mod = [f] + mod
        nums = list(range(1, n + 1))
        res = []
        for i in range(len(mod)):
            temp, k = k // mod[i], k % mod[i]
            res.append(temp)
        result = ""
        for i in range(len(res)):
            num = nums.pop(res[i])
            result += str(num)
        return result