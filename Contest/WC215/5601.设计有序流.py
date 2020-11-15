class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.vals = ["" for _ in range(n + 1)]
        self.ptr = 1


    def insert(self, id: int, value: str) -> List[str]:
        self.vals[id] = value
        if self.vals[self.ptr] == "":
            
            return []
        else:
            res = []
            while self.ptr < self.n + 1 and self.vals[self.ptr]:
                res.append(self.vals[self.ptr])
                self.ptr += 1
            return res



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)