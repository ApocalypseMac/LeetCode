class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n
        lh, rh = 0, 0
        result = 0
        for i in range(n):
            if height[i] > lh:
                lh = height[i]
            left[i] = lh
            if height[n - 1 - i] > rh:
                rh = height[n - 1 - i]
            right[n - 1 - i] = rh
        for i in range(n):
            h = min(left[i], right[i])
            if h > height[i]:
                result += h - height[i]
        return result