class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                res = max(res - 1, 0)
            else:
                res += 1
        return res