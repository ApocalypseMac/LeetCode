class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lo, hi = 0, 0
        while hi < len(nums):
            if nums[hi] == val:
                hi += 1
            else:
                nums[lo] = nums[hi]
                lo += 1
                hi += 1
        return lo
            
         