class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if arr[-1] - n < k:
            return k + n
        j = 0
        for i in range(1, arr[-1]):
            if i < arr[j]:
                k -= 1
                if k == 0:
                    return i
            else:
                j += 1