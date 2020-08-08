#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        currgas = 0
        start = 0
        curr = 0
        length = 0 # max length from start point
        while length < n:
            currgas += gas[curr]
            if currgas < cost[curr]: # cannot, reset
                start = curr + 1
                start %= n
                curr = start
                length = 0
                currgas = 0
            else:
                currgas -= cost[curr]
                curr += 1
                curr %= n
                length += 1
                
            
        
        return start
# @lc code=end

