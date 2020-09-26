#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        l = len(word)
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        visited = set()
        def helper(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == l - 1:
                return True
            visited.add((i, j))
            res = False
            for _ in range(4):
                ni, nj = i + dx[_], j + dy[_]
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    if helper(ni, nj, k + 1):
                        res = True
                        break
            visited.remove((i, j))
            return res
        
        for i in range(m):
            for j in range(n):
                if helper(i, j, 0):
                    return True
        return False
            
# @lc code=end

