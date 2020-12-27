class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        res = 0
        t1 = 0
        for t, cost in customers:
            t1 = max(t1, t)
            t1 += cost
            res += t1 - t
        return res / n