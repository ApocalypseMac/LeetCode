from math import atan, pi
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        maxview = 0
        def angleeval(dx, dy): # not same as loc.
            if dx == 0:
                if dy > 0:
                    return 90
                else:
                    return 270
            tan = dy / dx
            res = atan(tan) / pi * 180
            if dx < 0:
                res += 180
            return res
        angles = []
        lx, ly = location
        for x, y in points:
            dx, dy = x - lx, y - ly
            if dx == 0 and dy == 0:
                maxview += 1
                continue
            a = angleeval(dx, dy)
            angles += [a, a + 360]
        angles.sort()
        print(angles)
        max_ = 0
        n = len(angles)
        j = 0
        for i in range(n):
            while j < n and angles[j] - angles[i] <= angle + 10 ** -6:
                j += 1
            max_ = max(max_, j - i)
        return maxview + max_