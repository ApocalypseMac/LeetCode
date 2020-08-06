#
# @lc app=leetcode.cn id=1524 lang=python3
#
# [1524] 和为奇数的子数组数目
#

# @lc code=start
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0] & 1
        nodd, neven = 0, 1
        res = 0
        curr = 0
        for num in arr:
            curr += num
            curr &= 1
            if curr & 1:
                nodd += 1
                res += neven
            else:
                neven += 1
                res += nodd
            #print(res)
            res %= 10 ** 9 + 7
        return res
# @lc code=end

