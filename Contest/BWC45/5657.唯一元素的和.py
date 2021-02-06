class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = {}
        res = 0
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        for k, v in freq.items():
            if v == 1:
                res += k
        return res