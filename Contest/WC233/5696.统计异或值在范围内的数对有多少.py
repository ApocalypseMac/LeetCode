class Trie:
    def __init__(self):
        self.t = {}
    
    def insert(self, s):
        curr = self.t
        for ch in s:
            if '#' not in curr:
                curr['#'] = 0
            curr['#'] += 1
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        if '#' not in curr:
            curr['#'] = 0
        curr['#'] += 1

    
    def query(self, s1, limit, digit, curr):
        if digit < 0:
            return curr['#']
        p = 1 << (digit)
        ch = s1[16-digit]
        if ch == '1':
            och = '0'
        else:
            och = '1'
        res = 0
        if p > limit:
            if ch in curr:
                res += self.query(s1, limit, digit - 1, curr[ch])
        else:
            if och in curr:
                res += self.query(s1, limit - p, digit - 1, curr[och])
            if ch in curr:
                res += curr[ch]['#']
        # print(limit, digit, res, p)
        return res
        
        
        
class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        def tostr(num):
            res = ""
            for i in range(17):
                res += str(num % 2)
                num >>= 1
            return res[::-1]
        
        res = 0
        trie = Trie()
        
        for num in nums:
            s = tostr(num)
            hi = trie.query(s, high, 16, trie.t)
            lo = trie.query(s, low - 1, 16, trie.t)
            # print(num, hi, lo)
            res += hi - lo
            trie.insert(s)
            # print(trie.t)
            # print(tostr(num))
        
        return res
            