class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def box(i, j): # in which box
            return i // 3 * 3 + j // 3

        def rc(index): # index to row and column
            return (index // 9, index % 9)

        # used
        self.row = [[False] * 9 for _ in range(9)]
        self.col = [[False] * 9 for _ in range(9)]
        self.box = [[False] * 9 for _ in range(9)]
        
        # init
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    b = box(i, j)
                    self.row[i][num] = True
                    self.col[j][num] = True
                    self.box[b][num] = True
        
        def backtrack(board, index):
            if index == 81: # full
                return True # find answer
            r, c = rc(index)
            b = box(r, c)
            if board[r][c] != '.':
                return backtrack(board, index + 1) # to next site
            for i in range(9):
                if self.row[r][i] or self.col[c][i] or self.box[b][i]:
                    continue
                board[r][c] = str(i + 1)
                self.row[r][i] = True
                self.col[c][i] = True
                self.box[b][i] = True
                if backtrack(board, index + 1): # answer in subproblem
                    return True
                board[r][c] = '.'
                self.row[r][i] = False
                self.col[c][i] = False
                self.box[b][i] = False
            return False
        backtrack(board, 0)



            
            
            
        

        