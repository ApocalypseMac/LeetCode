class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        possible = [False] * (30001)
        for b in baseCosts:
            possible[b] = True
        for t in toppingCosts:
            for _ in range(2):
                for i in range(30000, -1, -1):
                    if possible[i] and i + t <= 30000:
                        possible[i+t] = True
        diff = 30000
        res = -1
        for i in range(30001):
            if possible[i]:
                if abs(target - i) < diff:
                    res = i
                    diff = abs(target - i)
        return res
        
    