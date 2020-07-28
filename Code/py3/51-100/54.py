class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return matrix
        m = len(matrix)
        n = len(matrix[0])
        rlo, rhi, clo, chi = 0, m - 1, 0, n - 1
        result = []
        while rlo <= rhi and clo <= chi:
            result += self.sprialLayer(matrix, rlo, rhi, clo, chi)
            rlo += 1
            rhi -= 1
            clo += 1
            chi -= 1
        
        return result
            
    def sprialLayer(self, matrix: List[List[int]], rlo: int, rhi: int, clo: int, chi: int):
        temp = []
        if rlo == rhi:
            for i in range(clo, chi + 1):
                temp.append(matrix[rlo][i])
            return temp
        elif clo == chi:
            for i in range(rlo, rhi + 1):
                temp.append(matrix[i][clo])
            return temp
        for i in range(clo, chi):
            temp.append(matrix[rlo][i])
        for i in range(rlo, rhi):
            temp.append(matrix[i][chi])
        for i in range(chi, clo, -1):
            temp.append(matrix[rhi][i])
        for i in range(rhi, rlo, -1):
            temp.append(matrix[i][clo])
        return temp
            
        
                
        
        