#
# @lc app=leetcode.cn id=1206 lang=python3
#
# [1206] 设计跳表
#

# @lc code=start
import random
import math
class Node:
    def __init__(self, val):
        self.val = val
        self.down = None
        self.next = None

class Skiplist:

    def __init__(self):
        self.maxlevel = 16
        self.left = [Node(-float('INF')) for _ in range(self.maxlevel)]
        self.right = [Node(float('INF')) for _ in range(self.maxlevel)]
        for i in range(self.maxlevel - 1):
            self.left[i].next = self.right[i]
            self.left[i].down = self.left[i + 1]
            self.right[i].down = self.right[i + 1]
        self.left[-1].next = self.right[-1]
        self.head = self.left[0] 

    # return random level (number of layers)   
    def _randlevel(self):
        rnd = self.maxlevel - int(math.log2(random.randint(1, 2 ** self.maxlevel - 1)))
        return rnd
    
    def _list(self):
        res = []
        curr = self.left[-1]
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

    def search(self, target: int) -> bool:
        curr = self.head
        while curr:
            if curr.next.val == target:
                return True
            elif curr.next.val < target:
                curr = curr.next
            else:
                curr = curr.down
        return False


    def add(self, num: int) -> None:
        level = self._randlevel()
        prev = []
        skipnode = [Node(num) for _ in range(level)]
        for i in range(level - 1):
            skipnode[i].down = skipnode[i + 1]
        curr = self.head
        while curr:
            if curr.next.val >= num:
                prev.append(curr)
                curr = curr.down
            else:
                curr = curr.next
        for p, n in zip(prev[-level:], skipnode):
            n.next = p.next
            p.next = n
        #print('add', num, self._list())

        
    def erase(self, num: int) -> bool:
        flag = False
        curr = self.head
        while curr:
            if curr.next.val > num:
                curr = curr.down
            elif curr.next.val < num:
                curr = curr.next
            else:
                flag = True
                # delete arbitrary ONE node
                curr.next = curr.next.next
                curr = curr.down
        #print('erase', num, self._list(), flag)
        return flag
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end

