class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        def digitone(num):
            ans = 0
            while num:
                if num & 1:
                    num -= 1
                    ans += 1
                num //= 2
            return ans
        
        for num in nums:
            res += digitone(num)
        maxval = max(nums)
        while maxval >= 2:
            res += 1
            maxval >>= 1
        return res
            