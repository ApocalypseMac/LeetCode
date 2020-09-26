#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def helper(nums, l, sum, start):
            if l == k:
                if sum == n:
                    res.append(nums)
                return
            elif sum + start > n:
                return 
            for i in range(start, 10):
                helper(nums + [i], l + 1, sum + i, i + 1)
            return
        
        helper([], 0, 0, 1)
        return res

# @lc code=end

