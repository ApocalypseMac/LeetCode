class Solution:
    def makeGood(self, s: str) -> str:
        while True:
            flag = False 
            res = ""
            i = 0
            n = len(s)
            while i < n - 1:
                #print(i, s[i], s[i + 1])
                if s[i].lower() == s[i + 1].lower() and ((s[i].islower() and s[i + 1].isupper()) or (s[i].isupper() and s[i + 1].islower())):
                    i += 2
                    flag = True
                else:
                    res += s[i]
                    i += 1
            while i < n:
                res += s[i]
                i += 1
            #print(res)
            if res == "" or flag == False:
                break
            s = res
        return res
            
            
        