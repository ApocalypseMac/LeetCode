class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        # greedy
        perfix = {0: -1}
        psum = 0
        intervals = []
        n = len(nums)
        for i in range(n):
            psum += nums[i]
            if psum - target in perfix:
                intervals.append([perfix[psum - target] + 1, i])
            perfix[psum] = i
        #print(intervals) # intervals sort in x[1]
        if intervals == []:
            return 0
        res = 1
        m = len(intervals)
        right = intervals[0][1]
        for interval in intervals:
            if interval[0] > right:
                res += 1
                right = interval[1]
        
        return res