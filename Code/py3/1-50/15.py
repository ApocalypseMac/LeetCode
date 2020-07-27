class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort + two pointers
        nums.sort()
        result = set()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            temp = -nums[i]
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                if nums[lo] + nums[hi] < temp:
                    lo += 1
                elif nums[lo] + nums[hi] > temp:
                    hi -= 1
                elif nums[lo] + nums[hi] == temp:
                    result.add((nums[i], nums[lo], nums[hi]))
                    lo += 1
                    hi -= 1
        return list(result)