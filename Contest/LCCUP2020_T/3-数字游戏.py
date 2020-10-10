import heapq
class Solution:
    def numsGame(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] -= i + 1
        #print(nums)
        res = []
        minheap = [] # larger
        maxheap = [] # smaller
        minsum, maxsum = 0, 0
        mincount, maxcount = 0, 0
        for i in range(n):
            heapq.heappush(maxheap, (-nums[i], nums[i]))
            _, maxtop = heapq.heappop(maxheap)
            maxsum += nums[i] - maxtop
            heapq.heappush(minheap, maxtop)
            mincount += 1
            minsum += maxtop
            if i % 2 == 0:
                mintop = heapq.heappop(minheap)
                minsum -= mintop
                mincount -= 1
                heapq.heappush(maxheap, (-mintop, mintop))
                maxsum += mintop
                maxcount += 1
            # find median
            if i % 2 == 0:
                m = maxheap[0][1]
            else:
                m = (maxheap[0][1] + minheap[0]) // 2
            #print(maxheap, minheap, m, maxsum, minsum)
            s1, s2 = m * maxcount , m * mincount
            #s3, s4 = (m + 1) * maxcount , (m + 1) * mincount
            res.append((s1 - maxsum + minsum - s2) % (10 ** 9 + 7))

        return res