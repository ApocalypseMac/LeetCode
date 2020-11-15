class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        if m < n:
            m, n = n, m
        k1, k2 = introvertsCount, extrovertsCount
        power = [3**_ for _ in range(n + 1)]
        l = 3 ** n
        masks = [[0] * n for _ in range(l)]
        cnt1, cnt2 = [0] * l, [0] * l
        scorel, scorell = [0] * l, [[0] * l for _ in range(l)]
        bonus = [[0, 0, 0], [0, -60, -10], [0, -10, 40]]
        base = [0, 120, 40]
        
        # preprocessing
        for mask in range(l):
            temp = mask
            for i in range(n):
                masks[mask][i] = temp % 3
                temp //= 3
            for i in range(n):
                state = masks[mask][i]
                if state == 1:
                    cnt1[mask] += 1
                    scorel[mask] += 120
                elif state == 2:
                    cnt2[mask] += 1
                    scorel[mask] += 40
                if i:
                    prevstate = masks[mask][i-1]
                    if state and prevstate:
                        scorel[mask] += bonus[state][prevstate]
        for pmask in range(l):
            for mask in range(l):
                for i in range(n):
                    scorell[mask][pmask] += bonus[masks[mask][i]][masks[pmask][i]]
        
        #print(scorel, scorell)
            
        #dp = [[[[0] * (k2 + 1) for _ in range(k1 + 1)] for _ in range(m + 1)] for _ in range(l)]
        @lru_cache(None)
        def helper(pmask, row, k1, k2):
            if row == m or k1 + k2 == 0:
                return 0
            res = 0
            for mask in range(l):
                if cnt1[mask] > k1 or cnt2[mask] > k2:
                    continue
                val = scorel[mask] + scorell[mask][pmask]
                val += helper(mask, row + 1, k1 - cnt1[mask], k2 - cnt2[mask])
                res = max(res, val)
            return res
        
        return helper(0, 0, k1, k2)
        
        
        ''' dfs (TLE)
        k1, k2 = introvertsCount, extrovertsCount
        bonus = [0, 40, 40 * 2 + 20 * 2, 40 * 3 + 20 * 4, 40 * 4 + 20 * 8, 40 * 5 + 20 * 10, 40 * 6 + 20 * 14]
        if m * n == 25:
            return 120 * k1 + bonus[k2]
        elif m * n == 20:
            if k1 < 6 or k2 < 6:
                return 120 * k1 + bonus[k2]
            else:
                return 120 * k1 + bonus[k2] - 10
        
        add = [120, 40]
        edge = [-30, 20]
        count = [k1, k2]
        grid = [[0] * n for _ in range(m)]
        res = 0
        #@lru_cache(None)
        def helper(site, val):
            nonlocal res
            if site == m * n or (count[0] == 0 and count[1] == 0):
                #print(val, count)
                res = max(res, val)
                return
            i, j = site // n, site % n
            grid[i][j] = 0
            helper(site + 1, val)
            for x in range(2):
                if count[x] == 0:
                    continue
                nval = val
                count[x] -= 1
                grid[i][j] = x + 1
                nval += add[x]
                if i > 0 and grid[i-1][j] > 0:
                    nval += edge[x] + edge[grid[i-1][j]-1]
                if j > 0 and grid[i][j-1] > 0:
                    nval += edge[x] + edge[grid[i][j-1]-1]
                helper(site + 1, nval)
                count[x] += 1
        helper(0, 0)
        return res
        '''
        