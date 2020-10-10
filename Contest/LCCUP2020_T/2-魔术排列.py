class Solution:
    def isMagic(self, target: List[int]) -> bool:
        def shuffle(deck):
            return deck[1::2] + deck[::2]
        n = len(target)
        deck = list(range(1, n + 1))
        # first shuffle decide k (greedily)
        deck = shuffle(deck)
        k = 0
        while k < n and deck[k] == target[k]:
            k += 1
        if k == 0:
            return False
        #print(k)
        deck = deck[k:]
        target = target[k:]
        n -= k
        # simulate remaining shuffle
        while n > 0:
            deck = shuffle(deck)
            if deck[:k] != target[:k]:
                return False
            deck = deck[k:]
            target = target[k:]
            n -= k
        return True