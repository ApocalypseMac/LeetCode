class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        left = [0] * (n + 2)
        lw = [0] * (n + 2)
        right = [0] * (n + 2)
        rw = [0] * (n + 2)
        for i in range(n):
            left[i+1] = left[i]
            lw[i+1] = lw[i] + left[i]
            if boxes[i] == '1':
                left[i+1] += 1
        for i in range(n - 1, -1, -1):
            right[i+1] = right[i+2]
            rw[i+1] = rw[i+2] + right[i+2]
            if boxes[i] == '1':
                right[i+1] += 1
        res = [lw[i+1] + rw[i+1] for i in range(n)]
        return res
        