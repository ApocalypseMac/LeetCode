class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        n = len(nums)
        m = len(groups)
        l = [len(groups[_]) for _ in range(m)]
        curr = 0
        i = 0
        while i < n and curr < m:
            if nums[i] == groups[curr][0]:
                if nums[i:i+l[curr]] == groups[curr]:
                    i += l[curr]
                    curr += 1
                    continue
            i += 1
        if curr == m:
            return True
        else:
            return False
                