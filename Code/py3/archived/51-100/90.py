class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.n = len(nums)
        res = []
        def backtrack(start, subset): # start at index start
            res.append(subset[:])
            if start == self.n:
                return
            n = len(nums)
            for i in range(start, n):
                if i > start and nums[i - 1] == nums[i]: # if duplicate, only process first one
                    continue
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
            return
        backtrack(0, [])
        return res