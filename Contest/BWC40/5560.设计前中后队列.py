#from collections import deque
class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []


    def pushFront(self, val: int) -> None:
        self.queue = [val] + self.queue


    def pushMiddle(self, val: int) -> None:
        mid = (len(self.queue)) // 2
        self.queue = self.queue[:mid] + [val] + self.queue[mid:]

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        if self.queue: 
            return self.queue.pop(0)
        else:
            return -1

    def popMiddle(self) -> int:
        mid = (len(self.queue) - 1) // 2
        if self.queue: 
            return self.queue.pop(mid)
        else:
            return -1

    def popBack(self) -> int:
        if self.queue: 
            return self.queue.pop()
        else:
            return -1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()