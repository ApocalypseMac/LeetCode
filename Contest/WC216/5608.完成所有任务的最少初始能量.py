class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: x[1] - x[0])
        #print(tasks)
        res = 0
        for act, min_ in tasks:
            res += act
            res = max(res, min_)
        return res
        
        