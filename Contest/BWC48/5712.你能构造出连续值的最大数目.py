class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        r = 1
        for v in coins:
            if v > r:
                return r
            else:
                r += v
        return r
        
        
        