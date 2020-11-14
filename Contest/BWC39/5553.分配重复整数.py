class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        freq = list(count.values())
        #print(freq)
        k = len(freq)
        m = len(quantity)
        l = 1 << (m)
        mask = [0] * l
        for i in range(l):
            for j in range(m):
                if i >> j & 1:
                    mask[i] += quantity[j]
        #print(quantity, mask)
        flag = False
        @lru_cache(None)
        def helper(state, idx):
            nonlocal flag
            if state + 1 == l:
                flag = True
                return
            if idx == k:
                return
            if flag:
                return
            helper(state, idx + 1)
            # enumerate subset
            m = (l - 1) ^ state
            x = m
            while x:
                if mask[x] <= freq[idx]:
                    helper(state | x, idx + 1)
                x = (x - 1) & m
            return
        helper(0, 0)
        
        return flag
            
            
            