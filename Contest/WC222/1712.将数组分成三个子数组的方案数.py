class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        psum = [0]
        n = len(nums)
        p = 0
        for num in nums:
            p += num
            psum.append(p)
        #print(n, p)
        #print(psum)
        res = 0 
        mod = 10 ** 9 + 7
        l, r = 1, 1
        # left: psum[i+1]
        # middle: psum[l+1] - psum[i+1]
        for i in range(n-2):
            left = psum[i+1]
            if left > p // 3 + 1:
                break
            if l <= i:
                l = i + 1
            while l < n - 1 and psum[l+1] - psum[i+1] < left:
                l += 1
            while r < n - 1 and psum[r+1] - psum[i+1] <= psum[-1] - psum[r+1]:
                r += 1
            #print(i, l, r)
            if r > l:
                res += r - l
        return res % mod