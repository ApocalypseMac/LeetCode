#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if words == [] and board == []:
            return []
        trie = {}
        def insert(T, word):
            for ch in word:
                if ch not in T:
                    T[ch] = {}
                T = T[ch]
            if '#' not in T: # mark end of the word
                T['#'] = word
        
        for word in words:
            insert(trie, word)
        
        m, n = len(board), len(board[0])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        found = set()
        visited = set()
        def helper(i, j, curr):
            if board[i][j] not in curr:
                return
            curr = curr[board[i][j]]
            if '#' in curr: # found word, not stop search
                found.add(curr['#'])
            visited.add((i, j))
            for _ in range(4):
                ni, nj = i + dx[_], j + dy[_]
                if 0 <= ni < m and 0 <= nj < n:
                    if (ni, nj) not in visited:
                        helper(ni, nj, curr)
            visited.remove((i, j))
            return
        
        for i in range(m):
            for j in range(n):
                helper(i, j, trie)



        return list(found)
        



# @lc code=end

