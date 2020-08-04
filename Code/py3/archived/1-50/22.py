class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # dp
        '''
        if n == 0:
            return [""]
        dp = [[""], ["()"]]
        for i in range(2, n + 1):
            result = []
            for j in range(i):
                for s1 in dp[j]:
                    for s2 in dp[i - 1 - j]:
                        result.append('(' + s1 + ')' + s2)
            dp.append(result)
        return dp[-1]
        '''
        # backtrack
        result = []
        def backtrack(s, l, r):
            if len(s) == 2 * n:
                result.append(s)
                return
            if l < n:
                s += '('
                backtrack(s, l + 1, r)
                s = s[:-1]
            if r < l:
                s += ')'
                backtrack(s, l, r + 1)
                s = s[:-1]
            return 
        backtrack('', 0, 0)
        return result