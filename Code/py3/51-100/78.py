class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtrack
        '''
        res = []
        self.n = len(nums)
        def backtrack(start, subset): # start at index start
            res.append(subset[:])
            if start == self.n:
                return
            n = len(nums)
            for i in range(start, n):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
            return
        backtrack(0, [])
        return res
        '''
        # loop
        '''
        res = [[]]
        for num in nums:
            for subset in res[:]:
                res.append(subset + [num])
        return res
        '''
        # recursion
        def helper(nums):
            if nums == []:
                return [[]]
            n = nums.pop()
            prev = helper(nums)
            res = prev[:]
            for subset in prev:
                res.append(subset + [n])
            return res
        return helper(nums)