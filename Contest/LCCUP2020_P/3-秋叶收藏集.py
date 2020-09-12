class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        cost = [float('INF')] * (n) # first i + 1 leaves yyyrrr min cost
        cost[0] = 0 if leaves[0] == 'r' else 1
        prey, prer = 0, 0
        y = [0] # num of yellow in i
        r = [0] # num of red in i
        for ch in leaves:
            if ch == 'y':
                prey += 1
            else:
                prer += 1
            y.append(prey)
            r.append(prer)
        #print(y, r)
        res = n
        for i in range(1, n - 1):
            # consider place i
            # 1 prev + yellow
            # 2 allred + yellow
            cost[i] = min(r[i+1] - r[i] + cost[i-1], r[i+1] - r[i] + y[i])           
            #print(i, cost[i] + prey - y[i+1])
            res = min(res, cost[i] + prey - y[i+1])
        #print(cost)    
        return res
        