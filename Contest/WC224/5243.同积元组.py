from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        prod = {}
        for i in range(n):
            for j in range(i + 1, n):
                p = nums[i] * nums[j]
                if p not in prod:
                    prod[p] = 0
                prod[p] += 1
        for v in prod.values():
            if v >= 2:
                res += 4 * v * (v - 1)
        return res