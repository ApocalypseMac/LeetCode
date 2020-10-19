class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        s = list(s)
        n = len(s)
        for i in range(n):
            s[i] = int(s[i])
        def compare(s1, s2):
            for i in range(n):
                if s1[i] < s2[i]:
                    return s1[:]
                elif s1[i] > s2[i]:
                    return s2[:]
                else:
                    continue
            return s1[:]
        def opa(s, a): # even
            for i in range(n // 2):
                s[2 * i + 1] += a
                s[2 * i + 1] %= 10
            return s
        def opa1(s, a): # odd
            for i in range(n // 2):
                s[2 * i] += a
                s[2 * i] %= 10
            return s
        def opb(s, b):
            return s[-b:] + s[:-b]
        min_ = s
        for i in range(10):
            for j in range(n):
                s = opb(s, b)
                min_ = compare(s, min_)
                #print(s, min_)
            s = opa(s, a)
        #print(s)
        if b & 1:
            for i in range(10):
                s = opa1(s, a)
                for j in range(10):
                    s = opa(s, a)
                    for k in range(n):
                        s = opb(s, b)
                        min_ = compare(s, min_)
                        #print(s, min_)
                    
        res = ""
        for i in range(n):
            res += str(min_[i])
        return res
        