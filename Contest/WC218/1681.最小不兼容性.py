class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = n // k
        print(m)
        if m == 1:
            return 0
        
        freq = {}
        state = [0] * 20
        for i in range(n):
            num = nums[i]
            if num not in freq:
                freq[num] = 0
            if freq[num] == k:
                return -1
            state[num] += 1 << i
            freq[num] += 1
        print(freq)
        if k == 1:
            return max(nums) - min(nums)
        
        
        mx = [0] * (2 ** n)
        mn = [1000] * (2 ** n)
        df = [1000] * (2 ** n)
        cnt = [0] * (2 ** n)
        for i in range(1, 2 ** n):
            for j in range(n):
                if i >> j == 1:
                    i1 = i ^ (1 << j)
                    if df[i1] == 2000:
                        df[i] = 2000
                    else:
                        mx[i] = max(mx[i1], nums[j])
                        mn[i] = min(mn[i1], nums[j])
                        if state[nums[j]] ^ i1 == state[nums[j]] | i1:
                            df[i] = mx[i] - mn[i]
                        else:
                            df[i] = 2000
                    cnt[i] = cnt[i1] + 1
        #print(mx)
        #print(mn)
        #print(df)
        #print(cnt)
        
        nstate = 1 << n - 1
        
        @lru_cache(None)
        def helper(unused):
            if unused == 0:
                return 0
            x = unused
            if cnt[unused] == m:
                return df[unused]
            res = float('INF')
            while x:
                if cnt[x] == m and df[x] != 2000:
                    res = min(res, df[x] + helper(unused ^ x))
                x = (x - 1) & unused
            #print(unused, res)
            return res

        return helper(2 ** n - 1)