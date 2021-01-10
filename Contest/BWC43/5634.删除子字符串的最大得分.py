class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        s = list(s)
        if x > y:
            a1 = 'a'
            b1 = 'b'
        else:
            a1 = 'b'
            b1 = 'a'
            x, y = y, x
        res = 0
        s1 = []
        for ch in s:
            if ch == b1 and s1 and s1[-1] == a1:
                s1.pop()
                res += x
            else:
                s1.append(ch)
        s2 = []
        for ch in s1:
            if ch == a1 and s2 and s2[-1] == b1:
                s2.pop()
                res += y
            else:
                s2.append(ch)
        return res