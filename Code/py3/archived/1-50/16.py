class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sort + two pointers
        nums.sort()
        mindiff = 4294967296
        for i in range(len(nums) - 2):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                currsum = nums[i] + nums[lo] + nums[hi]
                if currsum > target:
                    hi -= 1
                    if currsum - target < mindiff:
                        result = currsum
                        mindiff = currsum - target
                elif currsum < target:
                    lo += 1
                    if target - currsum < mindiff:
                        result = currsum
                        mindiff = target - currsum
                else:
                    return target
        return result