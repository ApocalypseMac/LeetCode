class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        ops = [0] * 26 # operation number freq
        if len(s) != len(t):
            return False
        n = len(s)
        for i in range(n):
            diff = ord(t[i]) - ord(s[i])
            if diff < 0:
                diff += 26
            if diff:
                ops[diff] += 1
        for i in range(1, 26):
            if ops[i] == 0:
                continue
            else:
                op = (ops[i] - 1) * 26 + i
                if op > k:
                    return False
        return True
            