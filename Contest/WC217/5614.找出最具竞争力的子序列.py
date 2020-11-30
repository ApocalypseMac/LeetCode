from collections import deque
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        cnt = len(nums) - k
        for n in nums:
            while stack and cnt and stack[-1] > n:
                stack.pop()
                cnt -= 1
            stack.append(n)
        while cnt:
            stack.pop()
            cnt -= 1
        return stack