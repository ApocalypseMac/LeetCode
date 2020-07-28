class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()
        def helper(currsum, startindex, curr):
            if currsum == target:
                res.append(curr)
                return 0
            elif startindex == n: # reach end
                return -1
            i = startindex + 1 # thus recursion start from -1
            while i < n:
                if currsum + candidates[i] > target:
                    break
                helper(currsum + candidates[i], i, curr + [candidates[i]])
                i += 1
                while i < n and candidates[i] == candidates[i - 1]: # remove duplicate
                    i += 1
            return 0

        helper(0, -1, [])
        return res