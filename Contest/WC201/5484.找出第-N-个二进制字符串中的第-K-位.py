class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        flip = 0
        powflag = False
        for i in range(n - 1, 0, -1):
            digit = (k >> i) & 1
            if digit == 0: # left part
                continue
            if digit == 1:
                if k == 1 << i:
                    flip += 1
                    break
                else:
                    flip += 1
                    k = (1 << (i + 1)) - k
            #print(k)
        #print('f', flip)
        ans = flip % 2
        return str(ans)