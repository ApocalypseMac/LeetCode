class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # hash set + two pointers
        nums.sort()
        result = set()
        for i in range(len(nums) - 3):
            if 4 * nums[i] > target:
                break
            if i > 0 and nums[i] == nums[i - 1]: # remove dup only at first layer of loop
                continue
            for j in range(i + 1, len(nums) - 2):
                if nums[i] + 3 * nums[j] > target:
                    break
                lo, hi = j + 1, len(nums) - 1
                temp = target - nums[i] - nums[j]
                while lo < hi:
                    if nums[lo] + nums[hi] > temp:
                        hi -= 1
                    elif nums[lo] + nums[hi] < temp:
                        lo += 1
                    else:
                        result.add((nums[i], nums[j], nums[lo], nums[hi])) # tuple is hashable
                        lo += 1
                        hi -= 1
        return list(result)