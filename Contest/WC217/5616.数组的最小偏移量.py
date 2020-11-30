from sortedcontainers import SortedList
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        def int2odd(n):
            while n & 1 == 0:
                n >>= 1
            return n
        arr = SortedList([])
        for num in nums:
            if num & 1:
                num <<= 1
            arr.add((int2odd(num), num))
        res = arr[-1][0] - arr[0][0]
        while arr[0][0] != arr[0][1]:
            n, cap = arr.pop(0)
            arr.add((n * 2, cap))
            res = min(res, arr[-1][0] - arr[0][0])
        return res