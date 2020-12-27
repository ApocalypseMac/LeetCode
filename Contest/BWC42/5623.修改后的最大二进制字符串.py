class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        n = len(binary)
        i = 0
        res = ''
        while i < n and binary[i] == '1':
            res += '1'
            i += 1
        if i >= n - 1:
            return binary
        cnt1 = 0
        n -= i
        for ch in binary[i:]:
            if ch == '1':
                cnt1 += 1
        if cnt1 >= n - 1:
            return binary
        else:
            res += '1' * (n - cnt1 - 1) + '0' + '1' * cnt1
            return res