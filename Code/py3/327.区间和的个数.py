#
# @lc app=leetcode.cn id=327 lang=python3
#
# [327] 区间和的个数
#

# @lc code=start
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0] # prefix sum
        for num in nums:
            prefix.append(prefix[-1] + num)
        def merge(dist, l, r):
            i, j = 0, 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    dist[i + j] = l[i]
                    i += 1
                else:
                    dist[i + j] = r[j]
                    j += 1
            if i < len(l):
                dist[i + j:] = l[i:]
            if j < len(r):
                dist[i + j:] = r[j:]
            return
        
        def countDiffLimit(l, r, limit):
            j, count = 0, 0
            for i, val in enumerate(l):
                while j < len(r) and r[j] - val <= limit:
                    j += 1
                count += j
            return count

        def countDiffRange(arr, lo, hi):
            if len(arr) <= 1:
                return 0
            mid = len(arr) // 2
            l, r = arr[:mid], arr[mid:]
            countl = countDiffRange(l, lo, hi)
            countr = countDiffRange(r, lo, hi)
            countx = countDiffLimit(l, r, hi) - countDiffLimit(l, r, lo - 1)
            merge(arr, l, r)
            return countl + countr + countx
        
        return countDiffRange(prefix, lower, upper)





            
# @lc code=end

