class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        n = len(arr)
        m = len(target)
        d = {}
        for i, num in enumerate(target):
            d[num] = i
        arr1 = []
        for i in range(n):
            if arr[i] in d:
                arr1.append(d[arr[i]])
        m1 = len(arr1)
        if m1 <= 1:
            return m - m1
        dp = [2 ** 31 - 1] * m1
        dp[0] = arr1[0]
        #print(arr1)
        res = 1
        for num in arr1[1:]:
            if num > dp[res-1]:
                dp[res] = num
                res += 1
            else:
                idx = bisect.bisect_left(dp, num, 0, res)
                #print(idx)
                dp[idx] = num
            #print(res, dp)
        return m - res
        