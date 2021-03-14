from heapq import heappush, heappop
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def cal(x, y):
            return (x + 1) / (y + 1) - x / y
        
        n = len(classes)
        pq = []
        for i in range(n):
            x, y = classes[i]
            heappush(pq, (-cal(x, y), i))
        for i in range(extraStudents):
            diff, idx = heappop(pq)
            classes[idx][0] += 1
            classes[idx][1] += 1
            x, y = classes[idx]
            heappush(pq, (-cal(x, y), idx))
            # print(idx, pq)
            
        res = 0
        for x, y in classes:
            res += x / y
        return res / n
                    
            
        