class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[lo] <= nums[mid]: # [lo, mid] sorted
                if nums[lo] <= target <= nums[mid]:
                    return self.searchsorted(nums, lo, mid, target)
                else:
                    lo = mid + 1
            else: #[mid + 1, hi]
                if nums[mid + 1] <= target <= nums[hi]:
                    return self.searchsorted(nums, mid + 1, hi, target)
                else:
                    hi = mid
        return -1
                
                
        
        
    # search in sorted subarray
    def searchsorted(self, nums, lo, hi, target: int) -> int:
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                return mid
        return -1