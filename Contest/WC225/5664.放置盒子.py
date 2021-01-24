class Solution:
    def minimumBoxes(self, n: int) -> int:
        l, r = 0, n + 1
        # optimized layout of one layer: a * a triangle + k extra cubes
        # optimized layout: a * a * a tetrahedron + k -- 1 extra cubes
        def para(num):
            l, r = 0, num
            while l < r:
                mid = l + (r - l) // 2
                if mid * (mid + 1) // 2 > num:
                    r = mid
                else:
                    l = mid + 1
            return l - 1, num - l * (l - 1) // 2
        
        # print(para(3), para(4))
        
        def check(n, num):
            a, k = para(num)
            res = a * (a + 1) * (a + 2) // 6 + k * (k + 1) // 2 
            return res >= n
        
        while l < r:
            mid = l + (r - l) // 2
            if check(n, mid):
                r = mid
            else:
                l = mid + 1
        return l