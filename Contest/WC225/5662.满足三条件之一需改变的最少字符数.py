class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        freqa = [0] * 26
        freqb = [0] * 26
        for ch in a:
            freqa[ord(ch) - ord('a')] += 1
        for ch in b:
            freqb[ord(ch) - ord('a')] += 1
        res = m + n
        for i in range(26): # op3
            res = min(res, m + n - freqa[i] - freqb[i])
        cnta = freqa[0]
        cntb = freqb[0]
        for i in range(1, 26): # op12
            res = min(res, m - cnta + cntb, n - cntb + cnta)
            cnta += freqa[i]
            cntb += freqb[i]
        return res
            
            