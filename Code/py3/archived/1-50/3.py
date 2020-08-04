class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window
        recentindex = {}
        maxlen = 0
        currlen = 0
        for i in range(len(s)):
            if s[i] not in recentindex:
                recentindex[s[i]] = i
                currlen += 1
            else:
                prev = recentindex[s[i]]
                recentindex[s[i]] = i
                currlen = min(currlen + 1, i - prev) # min of interval and curr + 1
            maxlen = max(maxlen, currlen) # calculate ma
        return maxlen