class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]
        i = 0
        while i < n and newInterval[0] > intervals[i][0]:
            i += 1
        if i == n: # edge case 1: insert at end
            result = intervals[:-1]
            intervals = [intervals[-1]] + [newInterval]
        elif i == 0: # edge case 2: insert at begin
            result = []
            intervals = intervals = [newInterval] + intervals
        else:
            result = intervals[:i - 1]
            intervals = [intervals[i - 1]] + [newInterval] + intervals[i:]
        start = intervals[0][0]
        end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] > end:
                result.append([start, end])
                start = interval[0]
                end = interval[1]
            else:
                end = max(end, interval[1])
        result.append([start, end])
        return result