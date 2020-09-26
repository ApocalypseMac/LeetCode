#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = {}
        shown = set()
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        stack = ['0']

        def greater(ch1, ch2):
            return ord(ch1) > ord(ch2)

        for ch in s:
            freq[ch] -= 1 
            if ch not in shown:
                while greater(stack[-1], ch) and freq[stack[-1]] > 0:
                    shown.remove(stack[-1])
                    stack.pop()
                stack.append(ch)
                shown.add(ch)
        return ''.join(stack[1:])
                
# @lc code=end

