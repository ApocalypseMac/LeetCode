class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        # n^4
        '''
        if len(s) > len(t):
            s, t = t, s
        n1, n2 = len(s), len(t)
        def check(s, t, i, j, k):
            fail = 0
            for _ in range(j-i):
                if s[i+_] != t[k+_]:
                    fail += 1
                    if fail > 1:
                        return False
            if fail == 1:
                #print(1, i, j, k)
                return True
            else:
                return False
        res = 0
        for i in range(n1):
            for j in range(i + 1, n1 + 1):
                for k in range(n2 + i - j + 1):
                    #print(i, j, k)
                    if check(s, t, i, j, k):
                        res += 1
        return res
        '''
        # n^3
        if len(s) > len(t):
            s, t = t, s
        n1, n2 = len(s), len(t)
        def check(s, t, i, j):
            fail = 0
            count = 0
            while i < n1 and j < n2:
                if s[i] != t[j]:
                    fail += 1
                    if fail > 1:
                        break
                if fail == 1:
                    count += 1
                i += 1
                j += 1
            return count
        
        res = 0
        for i in range(n1):
            for j in range(n2):
                res += check(s, t, i, j)  
        return res