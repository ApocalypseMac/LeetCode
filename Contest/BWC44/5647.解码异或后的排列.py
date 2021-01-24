class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        res = [0] * n
        # method 1: consider each bit
        # bitcnt = [0] * 18
        # for i in range(1, n + 1):
        #     idx = 0
        #     i1 = i
        #     while i1:
        #         if i1 & 1:
        #             bitcnt[idx] += 1
        #         i1 >>= 1
        #         idx += 1
        # # print(bitcnt)
        # x = 0
        # bitcnt1 = [0] * 18
        # for y in encoded:
        #     x ^= y
        #     x1 = x
        #     idx = 0
        #     while x1:
        #         if x1 & 1:
        #             bitcnt1[idx] += 1
        #         x1 >>= 1
        #         idx += 1
        # # print(bitcnt1)
        # for i in range(18):
        #     if bitcnt1[i] == bitcnt[i]:
        #         continue
        #     res[0] += 1 << i
        # method 2: xor get res[0]
        tmp = 0
        for i in range(1, n + 1):
            tmp ^= i
        for i in range(1, n - 1, 2):
            tmp ^= encoded[i]
        res[0] = tmp
        for i in range(1, n):
            res[i] = encoded[i-1] ^ res[i-1]
        return res
        