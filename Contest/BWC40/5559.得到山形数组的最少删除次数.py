class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        def lis(nums):
            res = [0] * n
            res[0] = 1
            for i in range(1, n):
                temp = 1
                for j in range(i):
                    if nums[j] < nums[i]:
                        temp = max(temp, res[j] + 1)
                res[i] = temp
            return res
        lis0 = lis(nums)
        lis1 = lis(nums[::-1])[::-1]
        res = n
        for i in range(1, n - 1):
            if lis0[i] >= 1 and lis1[i] >= 1:
                res = min(res, n - (lis0[i] + lis1[i] - 1))
        return res