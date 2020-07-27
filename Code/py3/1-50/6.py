class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 1 or numRows == 1:
            return s
        period = 2 * numRows - 2
        result = [""] * numRows
        for i in range(len(s)):
            mod = i % period
            if mod < numRows:
                result[mod] += s[i]
            else:
                result[period - mod] += s[i]
        res = ""
        for st in result:
            res += st
        return res