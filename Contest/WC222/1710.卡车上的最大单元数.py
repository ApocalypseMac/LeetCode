class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])
        res = 0
        for nb, nu in boxTypes:
            if truckSize > nb:
                res += nb * nu
                truckSize -= nb
            else:
                res += truckSize * nu
                return res
        return res
            