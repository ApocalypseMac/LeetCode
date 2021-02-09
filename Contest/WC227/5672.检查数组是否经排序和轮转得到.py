class Solution:
    def check(self, nums: List[int]) -> bool:
        nums1 = sorted(nums)
        n = len(nums)
        for i in range(n):
            if nums1 == nums[i:] + nums[:i]:
                return True
        return False