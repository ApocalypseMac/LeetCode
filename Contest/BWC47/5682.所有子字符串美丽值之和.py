class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            freq = defaultdict(int)
            for j in range(i, n):
                freq[s[j]] += 1
                # mx = -1
                # mn = 500
                # for v in freq.values():
                #     mx = max(mx, v)
                #     mn = min(mn, v)
                res += max(freq.values()) - min(freq.values())
        return res
                