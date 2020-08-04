class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        # queen: (col, r + c, r - c)
        def toStr(queen):
            #print('1')
            ans = []
            for i in queen:
                ans.append('.' * i[0] + 'Q' + '.' * (n - 1 - i[0]))
            return ans
        def isValid(q1, q2):
            return q1[0] != q2[0] and q1[1] != q2[1] and q1[2] != q2[2]
        def backtrack(queen):
            if len(queen) == n:
                res.append(toStr(queen))
                return
            row = len(queen)
            for col in range(n):
                flag = True
                q = (col, row + col, row - col)
                for i in range(len(queen)):
                    flag = isValid(queen[i], q)
                    if flag is False:
                        break
                if flag:
                    queen.append(q)
                    backtrack(queen)
                    queen.pop()
            return
        backtrack([])
        return res