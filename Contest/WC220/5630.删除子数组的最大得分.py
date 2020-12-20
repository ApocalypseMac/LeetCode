class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i = 0
        diffnum = set()
        n = len(nums)
        res = 0
        tmp = 0
        for j in range(n):
            tmp += nums[j]
            while nums[j] in diffnum:
                diffnum.remove(nums[i])
                tmp -= nums[i]
                i += 1
            diffnum.add(nums[j])
            res = max(res, tmp)
        return res