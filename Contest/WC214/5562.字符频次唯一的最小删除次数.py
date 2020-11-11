class Solution:
    def minDeletions(self, s: str) -> int:
        freq = {}
        for ch in s:
            if ch not in freq:
                freq[ch] = 0
            freq[ch] += 1
        v = list(freq.values())
        v.sort()
        setv = set(v)
        #print(v)
        res = 0
        for i in range(len(v) - 1):
            if v[i] == v[i+1]:
                while v[i] in setv and v[i]:
                    v[i] -= 1
                    res += 1
                if v[i] != 0:
                    setv.add(v[i])
        return res
        