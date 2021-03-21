class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        lo = 1
        hi = maxSum + 2
        l = index + 1
        r = n - index
        
        def check(mid, idx, n, mx):
            res = 0
            ll = mid - 1
            if l <= ll:
                lval = l * mid - l * (l - 1) // 2
            else:
                lval = ll * mid - ll * (ll - 1) // 2 + (l - ll)
            if r <= ll:
                rval = r * mid - r * (r - 1) // 2
            else:
                rval = ll * mid - ll * (ll - 1) // 2 + (r - ll)
            res += lval + rval
            res -= mid
            # print(n, mid, res)
            return res <= mx
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            # print(mid)
            if check(mid, index, n, maxSum):
                lo = mid + 1
            else:
                hi = mid
        return lo - 1
                
            
            
            
            