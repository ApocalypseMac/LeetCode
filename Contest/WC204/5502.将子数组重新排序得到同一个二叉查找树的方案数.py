#from scipy.special import comb
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return 0
        child = [[-1, -1] for _ in range(n + 1)]
        count = [0] * (n + 1)
        dp = [0] * (n + 1)
        root = nums[0]
        for num in nums[1:]:
            curr = root
            while True:
                if num < curr:
                    if child[curr][0] == -1:
                        child[curr][0] = num
                        break
                    else:
                        curr = child[curr][0]
                else:
                    if child[curr][1] == -1:
                        child[curr][1] = num
                        break
                    else:
                        curr = child[curr][1]
        #print(child)                
        def comb(n, m):
            return math.factorial(n) // (
                    math.factorial(m) * math.factorial(n - m))
        
        def helper1(node): # calculate count
            if count[node]:
                return count[node]
            if child[node] == [-1, -1]:
                count[node] = 1
            if child[node][0] != -1:
                lcount = helper1(child[node][0])
            else:
                lcount = 0
            if child[node][1] != -1:
                rcount = helper1(child[node][1])
            else:
                rcount = 0
            count[node] = lcount + rcount + 1
            return count[node]
        
        helper1(root)
        print(count)
        '''
        def helper(node):
            if dp[node] > 0:
                return dp[node]
            elif child[node] == [-1, -1]:
                dp[node] = 1
                return 1
            if child[node][0] != -1:
                dpl = helper(child[node][0])
                countl = count[child[node][0]]
            else:
                dpl = 0
                countl = 0
            if child[node][1] != -1:
                dpr = helper(child[node][1])
                countr = count[child[node][1]]
            else:
                dpr = 0
                countr = 0
            if dpl == 0:
                res = dpr
            elif dpr == 0:
                res = dpl
            else:
                res = dpl * dpr * int(comb(countl + countr, countl))
            res %= 10 ** 9 + 7
            dp[node] = res
            return res
        '''
        def helper(node):
            if dp[node] > 0:
                return dp[node]
            elif child[node] == [-1, -1]:
                dp[node] = 1
                return 1
            if child[node][0] != -1:
                dpl = helper(child[node][0])
                countl = count[child[node][0]]
            else:
                dpl = 1
                countl = 0
            if child[node][1] != -1:
                dpr = helper(child[node][1])
                countr = count[child[node][1]]
            else:
                dpr = 1
                countr = 0
            res = dpl * dpr * comb(countl + countr, countl)
            #res %= 10 ** 9 + 7
            dp[node] = res
            return res
        helper(root)
        print(dp)
        return (dp[root] - 1) % (10 ** 9 + 7)

            
        
        