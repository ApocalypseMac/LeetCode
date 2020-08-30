class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        minuscount = [0]
        mcount = 0
        for i in range(n):
            if nums[i] < 0:
                mcount += 1
            minuscount.append(mcount)
        #print(minuscount)
        
        def maxlen(lo, hi): # [lo, hi) without 0
            count = minuscount[hi] - minuscount[lo]
            if count % 2 == 0:
                return hi - lo
            for l in range(lo, hi + 1):
                if minuscount[l] - minuscount[lo] == 1:
                    break
            for r in range(hi, lo - 1, -1):
                if minuscount[hi] - minuscount[r] == 1:
                    break
            #print(hi, l, r, lo)
            return max(hi - l, r - lo)
        
        lo, hi = 0, 0
        while hi < n:
            if nums[hi] == 0:
                res = max(res, maxlen(lo, hi))
                hi += 1
                lo = hi
            else:
                hi += 1
        res = max(res, maxlen(lo, hi))
        
        return res
        