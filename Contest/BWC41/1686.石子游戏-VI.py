class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        values = list(zip(aliceValues, bobValues))
        values.sort(key = lambda x: -(x[0] + x[1]))
        a, b = 0, 0
        for i in range(n):
            if i & 1:
                b += values[i][1]
            else:
                a += values[i][0]
        if a > b:
            return 1
        elif a < b: 
            return -1
        else:
            return 0
        