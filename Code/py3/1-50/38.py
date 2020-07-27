class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = "1"
        for i in range(1, n):
            res = ""
            val = prev[0]
            count = 1
            for i in range(1, len(prev)):
                if prev[i] == val:
                    count += 1
                else:
                    res += str(count) + val
                    val = prev[i]
                    count =1
            res += str(count) + val
            prev = res
        return res