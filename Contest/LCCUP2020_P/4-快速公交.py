class Solution:
    def busRapidTransit(self, target: int, inc: int, dec: int, jump: List[int], cost: List[int]) -> int:
        n = len(jump)
        #choice = [(jump[i], cost[i]) for i in range(n)]
        #choice.sort(key = lambda x: )
        @lru_cache(None)
        def helper(pos):
            if pos == 1:
                return inc
            res = pos * inc
            for i in range(n):
                mod = pos % jump[i]
                mod1 = jump[i] - mod
                div = pos // jump[i]
                if div:
                    res = min(res, helper(div) + cost[i] + mod * inc) # multiply then inc
                if mod:
                    res = min(res, helper(div + 1) + cost[i] + mod1 * dec) # multiply then dec
            #print(pos, res)
            return res
        return helper(target) % (10 ** 9 + 7)
                
                
                    
        