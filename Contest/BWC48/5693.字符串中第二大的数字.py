class Solution:
    def secondHighest(self, s: str) -> int:
        val = set()
        for ch in s:
            if ch.isdigit():
                val.add(int(ch))
        val = sorted(list(val))[::-1]
        if len(val) < 2:
            return -1
        return val[1]