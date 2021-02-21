class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        res = ""
        i = 0
        while i < m and i < n:
            res += word1[i] + word2[i]
            i += 1
        while i < m:
            res += word1[i]
            i += 1
        while i < n:
            res += word2[i]
            i += 1
        return res