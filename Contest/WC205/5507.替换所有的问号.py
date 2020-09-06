class Solution:
    def modifyString(self, s: str) -> str:
        s = '#' + s + '#'
        res = '#'
        n = len(s)
        for i in range(1, n-1):
            if s[i] == '?':
                for j in range(26):
                    if chr(97 + j) != s[i-1] and chr(97 + j) != s[i+1] and chr(97 + j) != res[-1]:
                        res += chr(97 + j)
                        break
                    else:
                        continue
            else:
                res += s[i]
        return res[1:]
            
        