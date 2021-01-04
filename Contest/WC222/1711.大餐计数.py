class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        deliciousness.sort()
        mod = 10 ** 9 + 7
        d = dict()
        pow2 = [2 ** i for i in range(22)]
        res = 0
        for num in deliciousness:
            for p in pow2:
                if p - num > num + 1:
                    break
                if p - num in d:
                    res += d[p-num]
            if num not in d:
                d[num] = 0
            d[num] += 1
        return res % mod