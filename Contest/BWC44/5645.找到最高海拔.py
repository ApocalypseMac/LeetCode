class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        val = 0 
        res = 0
        for m in gain:
            val += m
            res = max(res, val)
        return res