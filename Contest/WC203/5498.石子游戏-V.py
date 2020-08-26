class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        # dp bottom-up (O(n^3), TLE)
        '''
        psum = 0
        perfix = [0]
        n = len(stoneValue)
        for i in range(n):
            psum += stoneValue[i]
            perfix.append(psum)
        dp = [[0] * (n) for _ in range(n)]
        # dp[i][j] : max val in [i, j]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                left = 0
                right = perfix[j + 1] - perfix[i]
                for k in range(i, j):
                    left += stoneValue[k]
                    right -= stoneValue[k]
                    #print(left, right)
                    if left < right:
                        temp = left + dp[i][k]
                    elif left > right:
                        temp = right + dp[k + 1][j]
                    else:
                        temp = max(left + dp[i][k], right + dp[k + 1][j])
                    dp[i][j] = max(dp[i][j], temp)
        #print(dp)
        return dp[0][-1]
        '''
        #dp top-bottom
        '''
        psum = 0
        perfix = [0]
        n = len(stoneValue)
        for i in range(n):
            psum += stoneValue[i]
            perfix.append(psum)
        #@lru_cache(None) 
        memo = {}
        def helper(l, r): # max val in [l, r]
            if (l, r) in memo:
                return memo[(l, r)]
            elif l == r:
                memo[(l, r)] = 0
                return 0
            elif l == r - 1:
                memo[(l, r)] = min(stoneValue[l], stoneValue[r])
                return min(stoneValue[l], stoneValue[r])
            left = 0
            right = perfix[r + 1] - perfix[l]
            res = 0
            for k in range(l, r):
                left += stoneValue[k]
                right -= stoneValue[k]
                #print(left, right)
                if left < right:
                    temp = left + helper(l, k)
                elif left > right:
                    temp = right + helper(k + 1, r)
                else:
                    temp = max(left + helper(l, k), right + helper(k + 1, r))
                res = max(res, temp)
            memo[(l, r)] = res
            return res
        return helper(0, n - 1)
        '''
        # dp O(n^2)
        psum = 0
        perfix = [0]
        n = len(stoneValue)
        for i in range(n):
            psum += stoneValue[i]
            perfix.append(psum)
        subsum = [[perfix[j + 1] - perfix[i] for j in range(n)] for i in range(n)]
        pos = [[0] * n for _ in range(n)] # [l, pos[l][r] - 1], L<R; [pos[l][r], r], L>=R
        opl = [[0] * n for _ in range(n)]
        opr = [[0] * n for _ in range(n)]
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            pos[i][i] = i
            curr = i
            for j in range(i + 1, n):
                while subsum[i][j] - subsum[i][curr] > subsum[i][curr]:
                    curr += 1
                pos[i][j] = curr
        #print(pos)
        for length in range(1, n + 1):
            for i in range(n + 1 - length):
                j = i + length - 1
                mid = pos[i][j]
                lsum = subsum[i][mid]
                rsum = subsum[mid+1][j] if mid + 1 < n else 0 # avoid exceed
                if lsum == rsum:
                    dp[i][j] = max(dp[i][j], opl[i][mid], opr[mid+1][j])
                else:
                    if mid > i:
                        lsum = subsum[i][mid-1]
                        dp[i][j] = max(dp[i][j], opl[i][mid-1])
                    if mid < j:
                        rsum = subsum[mid+1][j]
                        dp[i][j] = max(dp[i][j], opr[mid+1][j])
                val = dp[i][j] + subsum[i][j]
                if i == j:
                    opl[i][j] = opr[i][j] = val
                else:
                    opl[i][j] = max(val, opl[i][j-1])
                    opr[i][j] = max(val, opr[i+1][j])
        return dp[0][-1]




