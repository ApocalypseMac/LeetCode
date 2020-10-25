class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(nums)
        m = len(l)
        res = []
        def check(nums, li, ri):
            if ri == li + 1:
                return True
            arr = nums[li:ri+1]
            l = ri - li + 1
            arr.sort()
            d = arr[1] - arr[0]
            for i in range(2, l):
                if arr[i] - arr[0] != i * d:
                    return False
            return True
            
        for i in range(m):
            li, ri = l[i], r[i]
            res.append(check(nums, li, ri))
        return res
            