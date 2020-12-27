from collections import deque
class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        n = len(nums)
        psum = [0] # sum of zero and one
        occ1 = [] # 1 occurence place
        occ0 = [] # 0 occurence place
        pocc1 = [0] # sum of 1 occurence place
        pocc0 = [0] # sum of 0 occurence place
        p1 = 0
        p2 = 0
        p3 = 0
        for i in range(n):
            p1 += nums[i]
            psum.append(p1)
            if nums[i]:
                occ1.append(i)
                p2 += i
                pocc1.append(p2)
            else:
                occ0.append(i)
                p3 += i
                pocc0.append(p3)
        res = 2 ** 32 - 1  
        #print(psum)
        #print(occ1, occ0)
        #print(pocc1, pocc0)
        
        zeros = deque([])
        lo, hi = 0, k
        locc1, rocc1 = 0, 0
        locc0, rocc0 = 0, 0
        m = 0 # num of zeros
        for i in range(k):
            if nums[i] == 0:
                zeros.append(i)
                rocc0 += 1
                m += 1
            else:
                rocc1 += 1
        n1 = len(occ1)
        
        def val(rocc1, locc1, rocc0, locc0, m, n): # left: n, right: m - n
            #print(rocc1, locc1, rocc0, locc0)
            l, r = n, m - n
            lsum0 = pocc0[locc0 + l] - pocc0[locc0]
            rsum0 = pocc0[rocc0] - pocc0[locc0 + l]
            lsum1 = pocc1[locc1] - pocc1[locc1 - l]
            rsum1 = pocc1[rocc1 + r] - pocc1[rocc1]
            #print(lsum0, rsum0, lsum1, rsum1)
            return lsum0 - lsum1 + rsum1 - rsum0
        
        def search(rocc1, locc1, rocc0, locc0, lo, hi):
            
            while (hi - lo) >= 3:
                #print(hi, lo)
                tmp = (hi - lo) // 3
                m1, m2 = lo + tmp, hi - tmp
                #print(m1, m2)
                if val(rocc1, locc1, rocc0, locc0, m, m1) > val(rocc1, locc1, rocc0, locc0, m, m2):
                    lo = m1
                else:
                    hi = m2
            res = val(rocc1, locc1, rocc0, locc0, m, lo)
            for i in range(lo + 1, hi + 1):
                res = min(res, val(rocc1, locc1, rocc0, locc0, m, i))
            return res
    
        res = val(rocc1, locc1, rocc0, locc0, m, 0)
        
        for hi in range(k, n):
            if nums[hi - k]:
                locc1 += 1
            else:
                locc0 += 1
                zeros.popleft()
                m -= 1
            if nums[hi]:
                rocc1 += 1
            else:
                rocc0 += 1
                zeros.append(hi)
                m += 1
            if m == 0:
                return 0
            lc1 = locc1
            rc1 = n1 - rocc1
            ll, hh = max(0, m - rc1), min(m, lc1)
            #print(hi, lc1, rc1, ll, hh)
            res = min(res, search(rocc1, locc1, rocc0, locc0, ll, hh))
            #print(res)
        return res
