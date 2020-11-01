import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        steps = []
        n = len(heights)
        for i in range(n - 1):
            if heights[i] < heights[i+1]:
                steps.append((heights[i+1] - heights[i], i))
        #print(steps)
        if ladders >= len(steps):
            return n - 1
        pq = []
        for h, i in steps:
            heapq.heappush(pq, (h, i))
            if len(pq) > ladders:
                minh, _ = heapq.heappop(pq)
                if bricks - minh < 0:
                    return i
                bricks -= minh
            #print(pq)
        return n - 1
        