class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        l = max(min(w, h) for w, h in rectangles)
        res = 0
        for w, h in rectangles:
            if w > h:
                w, h = h, w
            if w >= l:
                res += 1
        return res