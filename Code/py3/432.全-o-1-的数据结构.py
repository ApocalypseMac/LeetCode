#
# @lc app=leetcode.cn id=432 lang=python3
#
# [432] 全 O(1) 的数据结构
#

# @lc code=start
class Node:
    def __init__(self, val):
        self.val = val
        self.keys = set()
        self.prev = None
        self.next = None
    
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # basic structure
        # 1. doubly linked list (each node means a frequency)
        # 2. set of keys in each (freq) node
        # 3. hash table: key -> freq
        # 4. hash table: freq -> node
        self.count = 0
        self.head = Node(-float('INF'))
        self.tail = Node(float('INF'))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.freq = {}
        self.value = {}
        #self.freq.setdefault(key, 0)
        #self.value.setdefault(key, None)


    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.freq: # exist
            f = self.freq[key]
            self.freq[key] += 1
            pred = self.value[f]
            if pred.next.val != f + 1:
                curr = Node(f + 1)
                self._addNodeAfter(curr, pred)
                self.value[f+1] = curr
            else:
                curr = pred.next
            curr.keys.add(key)
            pred.keys.remove(key)
            if len(pred.keys) == 0:
                self.value.pop(f)
                self._removeNode(pred)
        else: # not exist
            if self.head.next.val != 1:
                curr = Node(1)
                self._addNodeAfter(curr, self.head)
                self.value[1] = curr
            else:
                curr = self.head.next
            self.freq[key] = 1
            curr.keys.add(key)
            self.count += 1





    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.freq: # not in
            return
        else:
            f = self.freq[key]
            succ = self.value[f]
            succ.keys.remove(key)
            if f == 1: # freq == 1, delete
                self.freq.pop(key)
                self.count -= 1
            else: # freq > 1
                self.freq[key] -= 1
                if succ.prev.val != f - 1:
                    curr = Node(f - 1)
                    self._addNodeBefore(curr, succ)
                    self.value[f-1] = curr
                else:
                    curr = succ.prev
                curr.keys.add(key)
            if len(succ.keys) == 0:
                self.value.pop(f)
                self._removeNode(succ)


    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.count:
            maxset = self.tail.prev.keys
            key = maxset.pop()
            maxset.add(key)
            return key
        else:
            return ""


    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.count:
            minset = self.head.next.keys
            key = minset.pop()
            minset.add(key)
            return key
        else:
            return ""


    # remove specific node
    def _removeNode(self, curr) -> None:
        curr.next.prev = curr.prev
        curr.prev.next = curr.next
        del curr
    

    # add curr before succ
    def _addNodeBefore(self, curr, succ) -> None:
        pred = succ.prev
        pred.next = curr
        curr.prev = pred
        curr.next = succ
        succ.prev = curr
    

    # add curr after pred
    def _addNodeAfter(self, curr, pred) -> None:
        succ = pred.next
        succ.prev = curr
        curr.next = succ
        curr.prev = pred
        pred.next = curr

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end

