from sortedcontainers import SortedList
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        rem = SortedList([])
        for i in range(n):
            rem.add(i)
        diff = SortedList([])
        res = [-1] * n
        sim = SortedList([])
        def cal(i, j): # i < j
            pi, si = cars[i][0], cars[i][1]
            pj, sj = cars[j][0], cars[j][1]
            # print(i, j, si, sj)
            if si <= sj:
                return -1
            else:
                return (pj - pi) / (si - sj)
        for i in range(n - 1):
            time = cal(i, i + 1)
            if time != -1:
                sim.add((time, i, i + 1))
        # print(sim)
        while sim:
            # print(1)
            t, idx1, idx2 = sim[0]
            if res[idx1] > 0 and t > res[idx1]:
                del sim[0]
                continue
            res[idx1] = t
            del sim[0]
            rem.remove(idx1)
            # print(rem)
            ndx = rem.bisect_left(idx1)
            # print(ndx, rem[ndx - 1])
            if ndx and ndx > 0:
                time = cal(rem[ndx - 1], idx2)
                if time != -1:
                    sim.add((time, rem[ndx - 1], idx2))
            # print(sim)
            # print(rem)
            # print(res)
        return res
        
        