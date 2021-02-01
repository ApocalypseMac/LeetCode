from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n = len(adjacentPairs) + 1
        degree = defaultdict(int)
        edges = defaultdict(list)
        for u, v in adjacentPairs:
            edges[u].append(v)
            edges[v].append(u)
            degree[u] += 1
            degree[v] += 1
        res = []
        def helper(curr):
            while edges[curr]:
                succ = edges[curr].pop()
                helper(succ)
            res.append(curr)
            return
        
        tmp = None
        for k, v in degree.items():
            if v & 1:
                tmp = k
                break
        if tmp:
            helper(tmp)
        else:
            helper(adjacentPairs[0][1])
        return res[:n]