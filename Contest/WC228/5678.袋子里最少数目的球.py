class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        k = maxOperations
        def check(limit):
            cnt = 0
            for num in nums:
                cnt += (num - 1) // limit
            return cnt <= k
        
        lo, hi = 1, max(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
                    