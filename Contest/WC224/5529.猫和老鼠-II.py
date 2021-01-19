from collections import deque
from functools import lru_cache
class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        # dfs + memo
        m, n = len(grid), len(grid[0])
        dc, dm = catJump, mouseJump
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'M':
                    mi, mj = i, j
                elif grid[i][j] == 'C':
                    ci, cj = i, j
                elif grid[i][j] == 'F':
                    fi, fj = i, j
        
        # [cstate][mstate][round]
        # round: mouse: 0 cat: 1
        # value: win(this player): 1 lose: 0
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        
        # T: mouse win F: cat win
        @lru_cache(None)
        def helper(ci, cj, mi, mj, turn):
            if turn > 128: # in fact 70 will pass
                return False
            if turn & 1: # cat
                for k in range(4):
                    for s in range(dc + 1):
                        ni, nj = ci + s * dx[k], cj + s * dy[k]
                        if 0 <= ni < m and 0 <= nj < n:
                            if grid[ni][nj] == '#':
                                break
                            elif ni == fi and nj == fj:
                                return False
                            elif ni == mi and nj == mj:
                                return False
                            elif helper(ni, nj, mi, mj, turn + 1) is False: # mouse state, mouse lose
                                return False
                        else:
                            break
                return True
            else: # mouse
                for k in range(4):
                    for s in range(dm + 1):
                        ni, nj = mi + s * dx[k], mj + s * dy[k]
                        if 0 <= ni < m and 0 <= nj < n:
                            if grid[ni][nj] == '#':
                                break
                            elif ni == fi and nj == fj:
                                return True
                            elif ni == ci and nj == cj:
                                continue
                            elif helper(ci, cj, ni, nj, turn + 1): # cat state, cat lose
                                return True
                        else:
                            break
                return False
            
                
            
        return helper(ci, cj, mi, mj, 0)
        
#         # toposort + dp
#         m, n = len(grid), len(grid[0])
#         dc, dm = catJump, mouseJump
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 'M':
#                     mi, mj = i, j
#                 elif grid[i][j] == 'C':
#                     ci, cj = i, j
#                 elif grid[i][j] == 'F':
#                     fi, fj = i, j
        
#         # [cstate][mstate][round]
#         # round: mouse: 0 cat: 1
#         # value: win(this player): 1 lose: 0
#         state = [[[-1] * 2 for _ in range(64)] for _ in range(64)]
#         indeg = [[[0] * 2 for _ in range(64)] for _ in range(64)]
#         dx = [1, 0, -1, 0]
#         dy = [0, 1, 0, -1]
        
#         @lru_cache(None)
#         def s2c(state): # i, j
#             # print(state, (state // 8) % 8, state % 8)
#             return (state // 8) % 8, state % 8
        
#         def c2s(i, j):
#             return i * 8 + j
        
#         @lru_cache(None)
#         def nbs(i, j, step):
#             res = [i * 8 + j] # MUST contain itself
#             for _ in range(4):
#                 ci, cj = i, j
#                 di, dj = dx[_], dy[_]
#                 for k in range(1, step + 1):
#                     ci += di
#                     cj += dj
#                     if 0 <= ci < m and 0 <= cj < n and grid[ci][cj] != '#':
#                         res.append(8 * ci + cj)
#                     else:
#                         break
#             # if i == 0 and j == 3:
#             #     print(res, i, j, step)
#             return res
        
#         queue = deque([])
#         # same place, cat win
#         for i in range(m):
#             for j in range(n):
#                 s = i * 8 + j
#                 if grid[i][j] != '#' and grid[i][j] != 'F':
#                     state[s][s][0] = 0 
#                     state[s][s][1] = 1
#                     queue.append((s, s, 0))
#                     queue.append((s, s, 1))
        
#         sf = fi * 8 + fj
#         # reach food win
#         # will only go to **lose** state (nbs of lose states are win states)
#         for i in range(m):
#             for j in range(n):
#                 s = i * 8 + j
#                 if grid[i][j] != '#' and grid[i][j] != 'F':
#                     state[sf][s][0] = 0
#                     state[s][sf][1] = 0
#                     queue.append((sf, s, 0))
#                     queue.append((s, sf, 1))
        
#         # indeg
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] != '#': 
#                     s1 = i * 8 + j
#                     for k in range(m):
#                         for l in range(n):
#                             if grid[k][l] != '#': 
#                                 s2 = k * 8 + l
#                                 indeg[s1][s2][0] = len(nbs(k, l, dm))
#                                 indeg[s1][s2][1] = len(nbs(i, j, dc))            
#         # toposort
#         # in REVERSE order
#         while queue:
#             sc, sm, rd = queue.popleft()
#             if sc == ci*8+cj and sm == mi*8+mj and rd == 0:
#                 return state[sc][sm][rd] == 1
#             # print(sc, sm, rd, state[sc][sm][rd])
#             if rd: # cat turn, traverse mouse moves
#                 mx, my = s2c(sm)
#                 nb = nbs(mx, my, dm)
#                 for s in nb:
#                     indeg[sc][s][rd^1] -= 1
#                     if state[sc][s][rd^1] == -1: # undetermined
#                         if state[sc][sm][rd] == 0:
#                             state[sc][s][rd^1] = 1
#                             queue.append((sc, s, rd ^ 1))
#                         elif indeg[sc][s][rd^1] == 0:
#                             state[sc][s][rd^1] = 0
#                             queue.append((sc, s, rd ^ 1))      
#             else: # mouse turn, traverse cat moves
#                 cx, cy = s2c(sc)
#                 nb = nbs(cx, cy, dc)
#                 for s in nb:
#                     indeg[s][sm][rd^1] -= 1
#                     if state[s][sm][rd^1] == -1: # undetermined
#                         if state[sc][sm][rd] == 0:
#                             state[s][sm][rd^1] = 1
#                             queue.append((s, sm, rd ^ 1))
#                         elif indeg[s][sm][rd^1] == 0:
#                             state[s][sm][rd^1] = 0
#                             queue.append((s, sm, rd ^ 1))
            
#         return state[ci*8+cj][mi*8+mj][0] == 1