class Solution:
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        res = {}
        res[0] = (-1, -1)
        maxlen = 0
        state = 0
        for i in range(n):
            ch = ord(s[i]) - ord('0')
            state ^= (1 << ch)
            if state not in res:
                res[state] = (i, i)
            else:
                temp = res[state]
                res[state] = (temp[0], i)
        for i in res.keys():
            length = res[i][1] - res[i][0]
            for j in range(10):
                temp = i ^ (1 << j)
                if temp in res:
                    length = max(length, res[temp][1] - res[i][0], res[temp][0] - res[i][1])
            maxlen = max(length, maxlen)
        #print(res)
        return maxlen