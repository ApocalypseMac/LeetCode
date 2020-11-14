class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        code *= 3
        #print(code)
        res = [0] * n
        if k > 0:
            for i in range(n):
                res[i] = sum(code[n+i+1:n+i+k+1])
        elif k < 0:
            for i in range(n):
                res[i] = sum(code[n+i+k:n+i])
        return res