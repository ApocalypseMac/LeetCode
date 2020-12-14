class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        n = len(cuboids)
        for i in range(n):
            cuboids[i].sort()
        cuboids = sorted(cuboids)[::-1]
        # dp1
        '''
        #print(cuboids)
        dp = [[0] * 3 for _ in range(n)]
        dp[0] = cuboids[0]
        wl = [(1, 2), (0, 2), (0, 1)]
        for i in range(1, n):
            for k in range(3):
                ch = cuboids[i][k]
                cw, cl = wl[k]
                cw, cl = cuboids[i][cw], cuboids[i][cl]
                for j in range(i):
                    for l in range(3):
                        oh = cuboids[j][l]
                        ow, ol = wl[l]
                        ow, ol = cuboids[j][ow], cuboids[j][ol]
                        if cw <= ow and cl <= ol and ch <= oh:
                            dp[i][k] = max(dp[i][k], dp[j][l])
                dp[i][k] += cuboids[i][k]
        #print(dp)
        return max(max(dp[i]) for i in range(n))
        '''
        # dp2
        dp = [0] * n
        dp[0] = cuboids[0][2]
        for i in range(1, n):
            cw, cl, ch = cuboids[i]
            for j in range(i):
                ow, ol, oh = cuboids[j]
                if cw <= ow and cl <= ol and ch <= oh:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += cuboids[i][2]
        return max(dp)