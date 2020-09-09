#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set()
        maxlen = 0
        invl = {} # [l+1, r-1] store l
        invr = {} # [l+1, r-1] store r
        for num in nums:
            if num in visited: # avoid repeat
                continue
            else:
                visited.add(num)
                lo, hi = num, num
                if num in invl:
                    hi = invl[num][1]
                    invl.pop(num)
                if num in invr:
                    lo = invr[num][0]
                    invr.pop(num)
                maxlen = max(maxlen, hi - lo + 1)
                invl[lo - 1] = (lo, hi)
                invr[hi + 1] = (lo, hi)
        return maxlen

# @lc code=end

