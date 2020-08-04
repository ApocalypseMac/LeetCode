class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(curr, currlen, index):
            if currlen == k:
                res.append(curr)
                return
            elif index + k - currlen >= n: # end in advance if remaining numbers are not enough
                return 
            for i in range(index + 1, n):
                helper(curr + [i + 1], currlen + 1, i)
            return
        helper([], 0, -1)
        return res