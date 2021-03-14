class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = nums[k]
        l = k
        r = k
        for i in range(nums[k], 0, -1):
            while l >= 0 and nums[l] >= i:
                l -= 1
            while r < n and nums[r] >= i:
                r += 1
            res = max(res, i * (r - l - 1))
        return res
            
                
        
        
            
            
        