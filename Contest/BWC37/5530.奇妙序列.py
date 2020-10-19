class Fancy:

    def __init__(self):
        self.mod = 10 ** 9 + 7
        self.padd = []
        self.pmul = []
        self.add  = 0
        self.mul = 1
        self.vals = []
        


    def append(self, val: int) -> None:
        self.vals.append(val)
        self.padd.append(self.add)
        self.pmul.append(self.mul)


    def addAll(self, inc: int) -> None:
        self.add += inc

    def multAll(self, m: int) -> None:
        self.add *= m
        self.add %= self.mod
        self.mul *= m
        self.mul %= self.mod
        
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.vals):
            return -1
        val = self.vals[idx]
        oldadd = self.padd[idx]
        oldmul = self.pmul[idx]
        oldinvmul = pow(oldmul, self.mod - 2, self.mod)  # fermat's little theorem, inv(x) \equiv x ^ (p - 2) mod p
        # res = val * mul / oldmul + (add - oldadd * mul / oldmul)
        return ((val - oldadd) * self.mul * oldinvmul + self.add) % self.mod
        



# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)