#
# @lc app=leetcode.cn id=424 lang=python3
#
# [424] 替换后的最长重复字符
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if k >= n - 1:
            return n
        lo, hi = 0, 0 # [lo, hi)
        freq = [0] * 26
        maxfreq = 0 # history maxvalue
        for hi in range(n): # increase hi
            ch = ord(s[hi]) - ord('A')
            freq[ch] += 1
            maxfreq = max(maxfreq, freq[ch])
            if hi - lo + 1 > maxfreq + k: # if exceed
                ch1 = ord(s[lo]) - ord('A')
                freq[ch1] -= 1
                lo += 1
        return n - lo

        
# @lc code=end

