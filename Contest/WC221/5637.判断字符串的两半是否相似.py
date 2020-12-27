class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        set_ = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        n = len(s)
        s1, s2 = s[:n//2], s[n//2:]
        cnt1, cnt2 = 0, 0
        for ch in s1:
            if ch in set_:
                cnt1 += 1
        for ch in s2:
            if ch in set_:
                cnt2 += 1
        return cnt1 == cnt2