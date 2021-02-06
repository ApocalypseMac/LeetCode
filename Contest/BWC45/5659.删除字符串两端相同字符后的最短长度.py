class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            if s[l] != s[r]:
                break
            l1 = l + 1
            r1 = r - 1
            while l1 < n and s[l1] == s[l]:
                l1 += 1
            while r1 >= 0 and s[r1] == s[r]:
                r1 -= 1
            if r1 < l1:
                return 0
            l, r = l1, r1
            # print(l1, r1)
        return r - l + 1
        