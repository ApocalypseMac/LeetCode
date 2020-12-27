class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        min_ = min(nums)
        n, n1 = len(nums), len(queries)
        res = [0] * n1
        for i in range(n1):
            x, m = queries[i]
            # edge cases
            if m < min_: 
                res[i] = -1
                continue
            elif m == 0:
                res[i] = x
                continue
            # align the digits of binary strings
            dm = len(bin(m)) - 2
            xb = bin(x)[2:]
            mb = bin(m)[2:]
            if dm > len(xb):
                xb = '0' * (dm - len(xb)) + xb
            else:
                xb = xb[-dm:]
            #print(xb, mb)
            l = len(mb)
            # binary search
            base = 0
            lb, rb = nums[0], nums[bisect_right(nums, m) - 1] 
            #print(lb, rb)
            inv = 1 << (l) # length of interval
            d = -1
            while lb != rb:
                inv >>= 1
                d += 1
                if xb[d] == '1': # need 0
                    if lb >= base + inv: # miss
                        base += inv
                        continue
                    idx = bisect_left(nums, min(base + inv, rb + 1)) - 1 # maximum number smaller than min(base + inv, rb + 1)
                    rb = nums[idx]  # update rb
                else: # need 1
                    if rb < base + inv:
                        continue
                    idx = bisect_left(nums, max(base + inv, lb)) # maximum number greater than min(base + inv, lb)
                    lb = nums[idx]
                    base += inv    
            res[i] = x ^ lb
        return res
        