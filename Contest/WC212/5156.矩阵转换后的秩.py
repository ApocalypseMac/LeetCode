class UF:
    def __init__(self, n):
        self.count = [1] * n
        self.parent = [_ for _ in range(n)]
        self.rank = [1] * n
        
    def find(self, i): # find root(i) and compress the path
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j): # return if already connected
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            if self.count[pi] < self.count[pj]:
                pi, pj = pj, pi
            self.parent[pj] = pi
            self.count[pi] += self.count[pj]
            return False
        return True 
    
    # get and set rank from root
    def getrk(self, i):
        if 0 <= i < len(self.count):
            return self.rank[self.find(i)]
    
    # set: keep the larger value
    def setrk(self, i, val):
        if 0 <= i < len(self.count):
            self.rank[self.find(i)] = max(self.rank[self.find(i)], val)
        
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        
        # uf preprocessing (per row/col)
        uf = UF(m * n)
        for i in range(m):
            temp = list(enumerate(matrix[i]))
            temp.sort(key = lambda x: x[1])
            for j in range(n - 1):
                if temp[j][1] == temp[j+1][1]:
                    uf.union(i * n + temp[j][0], i * n + temp[j+1][0])
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append((j, matrix[j][i]))
            temp.sort(key = lambda x: x[1])
            for j in range(m - 1):
                if temp[j][1] == temp[j+1][1]:
                    uf.union(temp[j][0] * n + i, temp[j+1][0] * n + i)
        
        # sort and update rks
        res = [[0] * n for _ in range(m)]
        rowmax = [-1] * m # prevmaxrkidx
        colmax = [-1] * n
        nums = []
        for i in range(m):
            for j in range(n):
                nums.append([matrix[i][j], i, j])
        nums.sort()
        for val, i, j in nums:
            c = rowmax[i]
            r = colmax[j]
            if c == -1:
                rkr = 1
            else:
                rkr = uf.getrk(i * n + c)
                if matrix[i][c] != matrix[i][j]:
                    rkr += 1
            if r == -1:
                rkc = 1
            else:
                rkc = uf.getrk(r * n + j)
                if matrix[r][j] != matrix[i][j]:
                    rkc += 1
            rk = max(rkr, rkc)
            idx = i * n + j
            uf.setrk(idx, rk)
            rowmax[i] = j
            colmax[j] = i
        for i in range(m):
            for j in range(n):
                res[i][j] = uf.getrk(i * n + j)
    
        return res