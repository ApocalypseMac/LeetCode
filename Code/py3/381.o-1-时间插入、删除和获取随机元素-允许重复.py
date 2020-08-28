#
# @lc app=leetcode.cn id=381 lang=python3
#
# [381] O(1) 时间插入、删除和获取随机元素 - 允许重复
#

# @lc code=start
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = 0
        self.index = []
        self.elem = dict()



    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val not in self.elem:
            self.elem[val] = [self.count]
            self.index.append(val)
            self.count += 1
            return True
        else:
            self.elem[val].append(self.count)
            self.index.append(val)
            self.count += 1
            return False


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.elem:
            return False
        else:
            ind = self.elem[val]
            if len(ind) == 1:
                self.elem.pop(val)
                self.index[ind[0]] = None
            else:
                ind1 = ind.pop()
                self.index[ind1] = None
            return True


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        rnd = random.randint(0, self.count - 1)
        while self.index[rnd] is None:
            rnd = random.randint(0, self.count - 1)
        return self.index[rnd]



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

