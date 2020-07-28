class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        heights = [0] + heights + [0]
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                maxarea = max(maxarea, heights[index] * (i - 1 - stack[-1]) )
            stack.append(i)
        return maxarea