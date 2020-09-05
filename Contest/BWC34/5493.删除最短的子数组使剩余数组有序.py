class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        lo, hi = 0, n - 1
        while lo < n - 1:
            if arr[lo] <= arr[lo+1]:
                lo += 1
            else:
                break
        while hi > 0:
            if arr[hi] >= arr[hi-1]:
                hi -= 1
            else:
                break
        #print(lo, hi)
        if lo > hi:
            return 0
        res = min(n - 1 - lo, hi)
        l, r = 0, hi
        if arr[0] > arr[-1]:
            #print(1, n - lo - 1, hi)
            return res
        while l <= lo and r < n:
            while l <= lo and arr[l] <= arr[r]:
                l += 1
            #print(r, l)
            res = min(res, r - l)
            r += 1
        return res