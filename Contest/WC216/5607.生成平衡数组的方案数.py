class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        sum_ = sum(nums)
        presum = [[0, 0]]
        odd, even = 0, 0
        n = len(nums)
        for i in range(n):
            if i & 1:
                odd += nums[i]
            else:
                even += nums[i]
            presum.append([odd, even])
        #print(presum)
        res = 0
        for i in range(n):
            sodd = presum[i][0] + (presum[-1][1] - presum[i+1][1])
            if sodd * 2 == sum_ - nums[i]:
                res += 1
        return res
            
            
            
            