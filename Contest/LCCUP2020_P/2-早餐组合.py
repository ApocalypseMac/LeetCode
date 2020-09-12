class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        staple.sort()
        drinks.sort()
        m, n = len(staple), len(drinks)
        res = 0
        r = n - 1
        for l in range(m):
            temp = staple[l]
            while r >= 0 and drinks[r] + temp > x:
                r -= 1
            res += r + 1
            res %= 10 ** 9 + 7
        return res