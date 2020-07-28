class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key = lambda x: x[0])
        result = []
        start, end = intervals[0]
        for i in intervals[1:]:
            if i[0] > end:
                result.append([start, end])
                start = i[0]
                end = i[1]
            else:
                end = max(end, i[1])
        result.append([start, end])
        return result