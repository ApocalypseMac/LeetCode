class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        res = ""
        def check(s):
            s = set(s)
            for ch in s:
                if ch.islower() and ch.upper() in s:
                    continue
                if ch.isupper() and ch.lower() in s:
                    continue
                return False
            return True
        
        for i in range(n):
            for j in range(i + 1, n + 1):
                s1 = s[i:j]
                if check(s1) and len(s1) > len(res):
                    res = s1
        return res
                    