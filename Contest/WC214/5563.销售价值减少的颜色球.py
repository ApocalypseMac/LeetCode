class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        res = 0
        mod = 10 ** 9 + 7
        lo, hi = 0, max(inventory)
        def count(val):
            res = 0
            for num in inventory:
                if num > val:
                    res += num - val
            return res
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if count(mid) < orders:
                hi = mid
            else:
                lo = mid + 1
        
        #print(lo)
        res = lo * (orders - count(lo))
        for num in inventory:
            if num > lo:
                res += (num + lo + 1) * (num - lo) // 2
                res %= mod
        return res % mod
        
            