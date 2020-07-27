class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtrack
        result = []
        def backtrack(pnums, permutation):
            if pnums == []:
                result.append(permutation[:]) # need append a copy
                return
            for i in range(len(pnums)):
                permutation.append(pnums[i])
                backtrack(pnums[:i] + pnums[i+1:], permutation)
                permutation.pop()
            return
        backtrack(nums, [])
        return result
        '''
        result = []
        def backtrack(pnums, permutation):
            if pnums == []:
                result.append(permutation)
                return
            for i in range(len(pnums)):
                backtrack(pnums[:i] + pnums[i+1:], permutation + [pnums[i]])
            return
        backtrack(nums, [])
        return result
        '''