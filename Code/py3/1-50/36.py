class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = []
        col = []
        sbox = []
        for _ in range(9):
            row.append(set())
            col.append(set())
            sbox.append(set())
        def box(i, j):
            return i // 3 * 3 + j // 3
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row[i]:
                        return False
                    else:
                        row[i].add(board[i][j])
                    if board[i][j] in col[j]:
                        return False
                    else:
                        col[j].add(board[i][j])
                    if board[i][j] in sbox[box(i, j)]:
                        return False
                    else:
                        sbox[box(i, j)].add(board[i][j])
        return True