class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        step = -1
        invl = {} # [l+1, r-1] store l
        invr = {} # [l+1, r-1] store r
        for i, num in enumerate(arr):
            lo, hi = num, num
            if num in invl: # find right neighbor of num
                hi = invl[num][1]
                if invl[num][1] + 1 - invl[num][0] == m: # old interval length equals m, update step (this interval will change in step i + 1)
                    step = i
                invl.pop(num)
            if num in invr: # find left neighbor of num
                lo = invr[num][0]
                if invr[num][1]  + 1 - invr[num][0] == m: # old interval length equals m, update step
                    step = i
                invr.pop(num)
            #print(lo, hi)
            invl[lo - 1] = (lo, hi)
            invr[hi + 1] = (lo, hi)
        return step