class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        n = len(accounts)
        res = 0
        for i in range(n):
            res = max(res, sum(accounts[i]))
        return res