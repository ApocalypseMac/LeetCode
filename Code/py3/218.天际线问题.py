#
# @lc app=leetcode.cn id=218 lang=python3
#
# [218] 天际线问题
#

# @lc code=start
import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        points = []
        heap = [(0, float('INF'))] # (-h, r) since minheap
        res = [[0, 0]]

        for l, r, h in buildings:
            points.append((l, -h, r)) # left boundary
            points.append((r, 0, float('INF'))) # right boundary (consider as leftb of height 0)
        
        points.sort() # first length, then height (ascending)
        for l, h, r in points:
            while l >= heap[0][1]: # remove rightbs in heap left than l
                heapq.heappop(heap)
            if h < 0:
                heapq.heappush(heap, (h, r)) # add rightb and (negative) height
            if res[-1][1] != -heap[0][0]:
                res.append([l, -heap[0][0]])
        return res[1:]
        
# @lc code=end

