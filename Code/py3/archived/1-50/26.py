class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                length +=1
                nums[length] = nums[i]
        length += 1
        return length