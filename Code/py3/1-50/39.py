class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()
        def helper(currsum, startindex, curr):
            if currsum == target:
                res.append(curr)
                return 0
            for i in range(startindex, n):
                if currsum + candidates[i] > target:
                    break
                helper(currsum + candidates[i], i, curr + [candidates[i]])
            return 0

        helper(0, 0, [])
        return res