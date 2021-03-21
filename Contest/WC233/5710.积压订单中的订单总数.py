from heapq import heappush, heappop
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        buy = [] # maxheap
        sell = [] # minheap
        for p, n, idx in orders:
            if idx == 0:
                while n and sell and sell[0][0] <= p:
                    sp, sn = heappop(sell)
                    if n >= sn:
                        n -= sn
                    else:
                        sn -= n
                        n = 0
                        heappush(sell, (sp, sn))
                if n:
                    heappush(buy, (-p, n))
            else:
                while n and buy and -buy[0][0] >= p:
                    bp, bn = heappop(buy)
                    if n >= bn:
                        n -= bn
                    else:
                        bn -= n
                        n = 0
                        heappush(buy, (bp, bn))
                if n:
                    heappush(sell, (p, n))
        # print(sell, buy)
        res = 0
        for p, n in sell:
            res += n
        for p, n in buy:
            res += n
        return res % mod