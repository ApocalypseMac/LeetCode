class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        freq = {}
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = i
            else:
                res = max(res, i - freq[s[i]] - 1)
        return res