class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        req = {}
        window = {}
        m = len(s)
        res = ""
        minlen = m + 1
        for ch in t:
            if ch in req:
                req[ch] += 1
            else:
                req[ch] = 1
                window[ch] = 0
        print(req)
        l, r = 0, 0
        while r < m:
            print(window)
            if r in window:
                window[s[r]] += 1
            else:
                window[s[r]] = 1
            while all(map(lambda x: window[x] >= req[x], req.keys())):
                if r - l + 1 < minlen:
                    print(l, r)
                    res = s[l:r+1]
                    minlen = r - l + 1   
                window[s[l]] -= 1
                l += 1 
            r += 1
        return res