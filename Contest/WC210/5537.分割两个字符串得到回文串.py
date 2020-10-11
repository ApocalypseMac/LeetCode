class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)
        def ispd(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        if ispd(a) or ispd(b):
            return True
        if n & 1:
            start, end = n // 2, n // 2
        else:
            start, end = n // 2 - 1, n // 2
        sa, ea = start, end
        while a[sa] == a[ea]:
            sa -= 1
            ea += 1
        sb, eb = start, end
        while b[sb] == b[eb]:
            sb -= 1
            eb += 1
        #print(sa, ea, sb, eb)
        if a[:sa + 1] == b[ea:][::-1] or a[eb:] == b[:sb + 1][::-1] or b[:sa + 1] == a[ea:][::-1] or b[eb:] == a[:sb + 1][::-1]:
            return True
        return False
            