class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        res = 0
        n = len(points)
        for i in range(n-1):
            res = max(res, points[i+1][0] - points[i][0])
        return res