class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # shift in-place
        n = len(nums)
        for i in range(n):
            '''
            index = i
            temp = nums[i]
            # while not in correct place
            # end if exceed bound
            while 1 <= temp <= n and temp != index + 1: 
                index = temp - 1
                nums[index], temp = temp, nums[index]
                #print(nums, temp, index)
            '''
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]: 
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                #print(nums, temp, index)
        i = 0
        #print(nums)
        while i < n:
            if nums[i] != i + 1:
                return i + 1
            i += 1
        return i + 1
