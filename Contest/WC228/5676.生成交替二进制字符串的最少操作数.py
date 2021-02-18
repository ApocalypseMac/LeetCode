class Solution:
    def minOperations(self, s: str) -> int:
        odd0, odd1, even0, even1 = 0, 0, 0, 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '1':
                    even1 += 1
                else:
                    even0 += 1
            else:
                if s[i] == '1':
                    odd1 += 1
                else:
                    odd0 += 1
        return min(even1 + odd0, even0 + odd1)