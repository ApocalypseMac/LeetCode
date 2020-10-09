from sortedcontainers import SortedList
import heapq
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        n = len(arrival)
        busy = [] # heapq (emdtime, index)
        freq = [0] * k
        vacant = SortedList(range(k)) # ordered map (index)
        for i in range(n):
            mod = i % k
            a, l = arrival[i], load[i]
            while busy and busy[0][0] <= a:
                t, index = heapq.heappop(busy)
                vacant.add(index)
            if len(vacant) == 0: # no vacant server
                continue
            pos = vacant.bisect_left(mod)
            if pos == len(vacant):
                pos = 0
            server = vacant[pos]
            freq[server] += 1
            vacant.pop(pos)
            heapq.heappush(busy, (a + l, server))
            #print(busy, vacant)
        max_ = max(freq)
        res = []
        for i in range(k):
            if freq[i] == max_:
                res.append(i)
        #print(freq)
        return res