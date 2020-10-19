class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        for _ in range(n // 20):
            arr.pop(0)
            arr.pop()
        return sum(arr) / len(arr)