class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len(set(map(int, __import__("re").findall(r"\d+", word))))
                