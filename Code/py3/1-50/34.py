class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo1, lo2, hi1, hi2 = 0, 0, len(nums), len(nums)
        [left, right] = [-1, -1]
        # search left
        while lo1 < hi1:
            mid = lo1 + (hi1 - lo1) // 2
            if nums[mid] >= target:
                hi1 = mid
            else:
                lo1 = mid + 1
        left = lo1
        # search right
        while lo2 < hi2:
            mid = lo2 + (hi2 - lo2) // 2
            if nums[mid] <= target:
                lo2 = mid + 1
            else:
                hi2 = mid
        right = lo2 - 1
        if right < left:
            return [-1, -1]
        return [left, right]