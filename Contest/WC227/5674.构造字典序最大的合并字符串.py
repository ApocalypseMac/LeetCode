class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i, j = 0, 0
        res = ""
        
        def cmp(s1, s2, i, j):
            while i < m and j < n:
                if s1[i] > s2[j]:
                    return True
                elif s1[i] < s2[j]:
                    return False
                else:
                    i += 1
                    j += 1
            if i < m:
                return True
            else:
                return False

        while i < m and j < n:
            if cmp(word1, word2, i, j):
                res += word1[i]
                i += 1
            else:
                res += word2[j]
                j += 1
        while i < m:
            res += word1[i]
            i += 1
        while j < n:
            res += word2[j]
            j += 1
        return res