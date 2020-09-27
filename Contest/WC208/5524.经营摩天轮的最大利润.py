class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if runningCost > 4 * boardingCost:
            return -1
        maxcost = -float("INF")
        maxday = -1
        n = len(customers)
        cost = 0
        waiting = 0
        for i in range(n):
            c = customers[i]
            waiting += c - 4
            if waiting < 0:
                waiting = 0
            cost += boardingCost * min(4, c) - runningCost
            if cost > 0 and cost > maxcost:
                maxcost = cost
                maxday =  i
        if waiting:
            d = waiting // 4
            m = waiting % 4
            c1 = d * (4 * boardingCost - runningCost)
            c2 = waiting * boardingCost - runningCost * (d + 1)
            if c1 >= c2:
                day = n + d
                maxextra = c1
            else:
                day = n + d + 1
                maxextra = c2
            if maxextra + maxcost > 0 and maxextra + maxcost > maxcost:
                maxday = day
                
        return day
            
        
        
        