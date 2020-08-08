class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        curr = 0
        countr = 0
        i = 0
        for ch in s:
            if ch  == '(':
                if curr & 1:
                    res += 1
                    curr -= 1
                if curr < 0:
                    curr = -curr
                    res += (curr) // 2 # add '('s
                    curr = 0
                curr += 2
            else:
                countr += 1
                curr -= 1
            #print(countr)
        if curr < 0:
            curr = -curr
            if curr & 1:
                res += 2 # add "()"
            res += (curr) // 2 # add '('s
            curr = 0
        elif curr > 0:
            res += curr
        return res