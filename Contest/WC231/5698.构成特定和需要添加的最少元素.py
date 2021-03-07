class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        s = sum(nums)
        diff = abs(s - goal)
        if diff == 0:
            return 0
        else:
            return 1 + (diff - 1) // limit