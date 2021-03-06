class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = -1
        mval = 999999
        n = len(points)
        for i in range(n):
            xx = points[i][0]
            yy = points[i][1]
            if xx == x or yy == y:
                if abs(x - xx) + abs(y - yy) < mval:
                    res = i
                    mval = abs(x - xx) + abs(y - yy)

        return res