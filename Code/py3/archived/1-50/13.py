class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        s += 'I'
        number = 0
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(n):
            if mapping[s[i]] >= mapping[s[i + 1]]:
                number += mapping[s[i]]
            else:
                number -= mapping[s[i]]
        return number