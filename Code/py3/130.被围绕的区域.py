#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == []:
            return
        queue = deque([])
        m = len(board)
        n = len(board[0])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for i in range(m):
            if board[i][0] == 'O':
                queue.append((i, 0))
            if board[i][n-1] == 'O':
                queue.append((i, n-1))
        for j in range(n):
            if board[0][j] == 'O':
                queue.append((0, j))
            if board[m-1][j] == 'O':
                queue.append((m-1, j))
        
        while queue:
            currx, curry = queue.popleft()
            board[currx][curry] = '+'
            for _i in range(4):
                if 0 <= currx + dx[_i] < m and 0 <= curry + dy[_i] < n and board[currx + dx[_i]][curry + dy[_i]] == 'O':
                    queue.append((currx + dx[_i], curry + dy[_i]))

                



        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '+':
                    board[i][j] = 'O'
                    

                    

# @lc code=end

