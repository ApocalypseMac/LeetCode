from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        mod = 10 ** 9 + 7
        nums = SortedList([])
        res = 0
        #nums.add(instructions[0])
        #for num in instructions[1:]:
        for num in instructions:
            l = nums.bisect_left(num)
            r = len(nums) - nums.bisect_right(num)
            res += min(l, r)
            nums.add(num)
        return res % mod
            