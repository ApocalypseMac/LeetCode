class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted([a, b, c])
        if c >= a + b:
            return a + b
        return (a + b + c) // 2