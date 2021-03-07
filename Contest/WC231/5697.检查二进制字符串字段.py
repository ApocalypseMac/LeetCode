class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        cnt = 0
        s = '0' + s
        n = len(s)
        for i in range(n - 1):
            if s[i+1] == '1':
                if s[i] == '0':
                    cnt += 1
            if cnt > 1:
                return False
        return True
            