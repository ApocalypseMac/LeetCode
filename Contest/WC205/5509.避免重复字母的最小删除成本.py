class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        # dp (shrink char set)
        '''
        n = len(s)
        if n == 1:
            return 0
        
        ab = dict()
        #ba = dict()
        alen = 0
        for i in range(26):
            if chr(97 + i) in s:
                ab[chr(97 + i)] = alen
                #ba[alen] = chr(97 + i)
                alen += 1
        #print(ab)
        
        dp = [[0] * (alen + 1) for _ in range(n + 1)] # s[:i], end in j
        for j in range(alen):
            dp[0][j] = 0
        dp[1][ab[s[0]]] = 0
        
        prefix = 0
        psum = [0]
        for i in range(n):
            prefix += cost[i]
            psum.append(prefix)
        #print(psum)
        
        diff = [0] # last diff in psum
        curr = 0
        for i in range(1, n):
            if s[i] != s[i-1]:
                curr = i
            diff.append(curr)
        #print(diff)
        
        for i in range(2, n + 1):
            index = ab[s[i-1]]
            for j in range(alen):
                dp[i][j] = dp[i-1][j] + cost[i-1] # delete i-1
                if j != index: 
                    continue
                else: # keep i or keep same ch before i
                    temp = dp[i][j]
                    for k in range(alen):
                        if k != index:
                            temp = min(temp, dp[i-1][k])
                        else:
                            #print(temp)
                            lastdiff = diff[i-1]
                            for m in range(alen):
                                temp = min(temp, dp[lastdiff][m] + psum[i-1] - psum[lastdiff])
                                
                    dp[i][j] = temp      
        #print(dp)
        res = min(dp[-1][i] for i in range(alen))
        return res
        '''

        # greedy
        '''
        res = 0
        n = len(s)
        if n <= 1:
            return 0
        i = 0
        while i < n - 1:
            if s[i] != s[i+1]:
                i += 1
                continue
            r = i
            while r < n - 1 and s[r] == s[r+1]:
                r += 1
            res += sum(cost[i:r+1]) - max(cost[i:r+1])
            i = r
        return res
        '''
        
        # onepass greedy
        res = 0
        n = len(s)
        prevcost = cost[0]
        for i in range(1, n):
            if s[i] == s[i-1]:
                res += min(cost[i], prevcost)
                prevcost = max(cost[i], prevcost)
            else:
                prevcost = cost[i]
        return res
