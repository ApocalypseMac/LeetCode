class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort(key = lambda x: -x)
        #print(piles)
        res = 0
        for i in range(n // 3):
            res += piles[2 * i + 1]
        return res