class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        n = len(s1)
        for i in range(n):
            for j in range(i):
                flag = True
                for k in range(n):
                    if k == i:
                        if s1[j] != s2[k]:
                            flag = False
                            break
                    elif k == j:
                        if s1[i] != s2[k]:
                            flag = False
                            break
                    else:
                        if s1[k] != s2[k]:
                            flag = False
                            break
                if flag:
                    return True
        return False
                        
                