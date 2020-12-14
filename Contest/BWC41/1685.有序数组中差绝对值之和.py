class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tmp = sum(nums[i] - nums[0] for i in range(1, n))
        res = [tmp]
        for i in range(1, n):
            delta = nums[i] - nums[i-1]
            tmp += delta * (i - 1)
            tmp -= delta * (n - 1 - i)
            res.append(tmp)
        return res
            