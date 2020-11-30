class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        freq = {}
        res = n
        left = []
        right = []
        for i in range(n//2):
            temp = nums[i] + nums[n-1-i]
            if temp not in freq:
                freq[temp] = 0
            freq[temp] += 1
            lo = min(nums[i], nums[n-1-i]) + 1
            hi = max(nums[i], nums[n-1-i]) + limit + 1
            left.append(lo)
            right.append(hi)
        left.sort()
        left = [0] + left + [3 * limit]
        right.sort()
        right = [0] + right + [3 * limit]
        sums = list(freq.keys())
        sums.sort()
        #print(left, right, sums)
        l, r = 0, 0
        for s in sums:
            while left[l] <= s:
                l += 1
            while right[r] <= s:
                r += 1
            #print(s, n - freq[s] - l + r)
            res = min(res, n - freq[s] - l + r)
        return res
                