class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        n1 = 0
        degree = [0] * n
        reqs = []
        for req in requests:
            if req[0] == req[1]:
                n1 += 1
            else:
                reqs.append(req)
        m = len(reqs)
        self.res = n1
        def helper(i, num):
            if i == m:
                return
            for k in range(i, m):
                f, t = reqs[k]
                degree[f] += 1
                degree[t] -= 1
                num += 1
                if all(degree[i] == 0 for i in range(n)):
                    self.res = max(self.res, n1 + num)
                helper(k + 1, num)
                degree[f] -= 1
                degree[t] += 1
                num -= 1
            return
        helper(0, 0)
        return self.res
                
                