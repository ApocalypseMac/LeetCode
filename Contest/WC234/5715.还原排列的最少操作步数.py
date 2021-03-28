class Solution:
    def reinitializePermutation(self, n: int) -> int:
        res = 1  
        curr = n // 2
        while curr != 1:
            if curr & 1:
                curr = n // 2 + curr // 2
            else:
                curr //= 2
            res += 1
        return res
                