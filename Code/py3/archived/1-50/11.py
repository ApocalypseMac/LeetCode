class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            h = 0
            dis = r - l
            if height[l] < height[r]:
                h = height[l]
                l += 1
            else:
                h = height[r]
                r -= 1
            area = dis * h
            if area > max_area:
                max_area = area
        return max_area