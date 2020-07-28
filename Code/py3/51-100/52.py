class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        # queen: (col, r + c, r - c)
        def isValid(q1, q2):
            return q1[0] != q2[0] and q1[1] != q2[1] and q1[2] != q2[2]
            #return all(x != y for x, y in zip(q1, q2))
        def backtrack(queen):
            if len(queen) == n:
                self.res += 1
                return
            row = len(queen)
            for col in range(n):
                flag = True
                q = (col, row + col, row - col)
                for i in range(len(queen)):
                    if isValid(queen[i], q) is False:
                        flag = False
                        break
                if flag:
                    queen.append(q)
                    backtrack(queen)
                    queen.pop()
            return
        backtrack([])
        return self.res