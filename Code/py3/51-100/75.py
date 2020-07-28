class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo, hi = 0, len(nums) - 1
        curr = 0
        while curr <= hi:
            if nums[curr] == 0:
                nums[curr], nums[lo] = nums[lo], nums[curr]
                lo += 1
                curr += 1
            elif nums[curr] == 2: # this case curr will not add one since exchanged curr has not been scanned
                nums[curr], nums[hi] = nums[hi], nums[curr]
                hi -= 1
            else:
                curr += 1