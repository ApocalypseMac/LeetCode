from math import sqrt
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        eps = 10 ** -7
        def d(x1, y1, x2, y2):
            return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        def intensity(towers, x, y, radius):
            res = 0
            for x1, y1, q in towers:
                dis = d(x1, y1, x, y)
                if dis < radius + eps:
                    res += int(q / (1 + dis))
            return res
        maxintensity = 0
        maxpos = (0, 0)
        for x in range(51):
            for y in range(51):
                i = intensity(towers, x, y, radius)
                if i > maxintensity:
                    maxpos = (x, y)
                    maxintensity = i
        return maxpos
                    
                