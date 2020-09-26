#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

# @lc code=start
# method 1: maxheap + minheap
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # maxheap have the same or larger element than minheap
        self.count = 0
        self.maxheap = [] # smaller (-num, num)
        self.minheap = [] # larger num
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, (-num, num))
        _, maxtop = heapq.heappop(self.maxheap)
        heapq.heappush(self.minheap, maxtop)
        self.count += 1
        if self.count & 1: #if odd, move one element from minheap to maxheap
            mintop = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, (-mintop, mintop))
        

    def findMedian(self) -> float:
        if self.count & 1:
            return self.maxheap[0][1]
        else:
            return (self.maxheap[0][1] + self.minheap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

