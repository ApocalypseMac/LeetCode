#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 重复 N 次的元素
#

# @lc code=start
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        n = len(A)
        for interval in range(1, 4): # edge case: [1,2,3,1]
            for i in range(n - interval):
                if A[i] == A[i + interval]:
                    return A[i]
# @lc code=end

