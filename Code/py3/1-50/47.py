class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        def backtrack(curr, used, currlen):
            if currlen == n:
                res.append(curr)
                return 0
            i = 0
            while i < n:
                if used[i]:
                    i += 1
                    continue
                backtrack(curr + [nums[i]], used[:i] + [True] + used[i + 1:], currlen + 1) # if i > n, a[i:] = []
                i += 1
                while i < n and nums[i] == nums[i - 1]:
                    i += 1
            return 0
                
                
        backtrack([], [False] * n, 0)
        return res

