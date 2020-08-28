#
# @lc app=leetcode.cn id=838 lang=python3
#
# [838] 推多米诺
#

# @lc code=start
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        num = 0
        ops = []
        nums = []
        for ch in dominoes:
            if ch == '.':
                num += 1
            else:
                ops.append(ch)
                nums.append(num)
                num = 0
        nums.append(num)
        #print(ops, nums)
        n = len(nums)
        ops = ['L'] + ops + ['R']
        res = ""
        for i in range(n):
            opl, opr = ops[i], ops[i + 1]
            res += opl
            if nums[i]:
                if opl == 'R' and opr == 'L':
                    res += 'R' * (nums[i] // 2) + '.' * (nums[i] % 2) + 'L' * (nums[i] // 2)
                elif opl == 'R':
                    res += 'R' * nums[i]
                elif opr == 'L':
                    res += 'L' * nums[i]
                else:
                    res += '.' * nums[i]
        return res[1:]


        
        
# @lc code=end

