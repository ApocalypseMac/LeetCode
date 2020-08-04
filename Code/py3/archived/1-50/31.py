class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]: # may have elements of same value
            i -= 1
        def swap(i):
            lo, hi = i, len(nums) - 1
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1
        if i == 0:
            swap(0)
        else:
            j = i
            while j < len(nums) and nums[j] > nums[i - 1]:
                j += 1
            nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]
            swap(i)
        return nums