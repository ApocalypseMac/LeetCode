from sortedcontainers import SortedDict
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        res = 0
        n = len(days)
        queue = SortedDict([])
        for i in range(n):
            k = apples[i]
            d = i + days[i] - 1
            if k:
                if d not in queue:
                    queue[d] = 0
                queue[d] += k
            if queue:
                key, val = queue.peekitem(0)
                if val == 1:
                    del queue[key]
                res += 1
            if i in queue:
                queue.pop(i) 
        days = n
        while queue:
            key, val = queue.peekitem(0)
            if val == 1:
                queue.pop(key)
            res += 1
            
            if days in queue:
                queue.pop(days)
            days += 1
        return res