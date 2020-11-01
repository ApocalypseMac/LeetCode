class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pos = {}
        for i in range(len(pieces)):
            pos[pieces[i][0]] = (i, len(pieces[i]))
        i = 0
        used = [False] * len(pieces)
        while i < len(arr):
            if arr[i] not in pos:
                return False
            p, delta = pos[arr[i]]
            if i + delta > len(arr):
                return False
            if arr[i:i+delta] != pieces[p]:
                return False
            i += delta
        return True