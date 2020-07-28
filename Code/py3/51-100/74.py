class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0 or target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        rlo, rhi = 0, m
        while rlo < rhi:
            rmid = rlo + (rhi - rlo) // 2
            if target > matrix[rmid][-1]: # compare with last element of rach row
                rlo = rmid + 1
            elif target < matrix[rmid][-1]:
                rhi = rmid
            else:
                return True
        clo, chi = 0, n - 1
        while clo <= chi:
            cmid = clo + (chi - clo) // 2
            if target > matrix[rlo][cmid]:
                clo = cmid + 1
            elif target < matrix[rlo][cmid]:
                chi = cmid - 1
            else:
                return True
        return False