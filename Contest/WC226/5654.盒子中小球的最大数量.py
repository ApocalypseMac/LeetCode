class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        cnt = {}
        for i in range(lowLimit, highLimit + 1):
            tmp = 0
            while i:
                tmp += i % 10
                i //= 10
            if tmp not in cnt:
                cnt[tmp] = 0
            cnt[tmp] += 1
        # print(cnt)
        return max(cnt.values())