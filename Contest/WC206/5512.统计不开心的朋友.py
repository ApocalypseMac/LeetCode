class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        if n == 2:
            return 0
        relation = [[0] * n for _ in range(n)]
        pair = dict()
        for i in range(n):
            for j in range(n - 1):
                relation[i][preferences[i][j]] = n - 1 - j
        #print(relation)
        for x, y in pairs:
            pair[x] = (y, relation[x][y])
            pair[y] = (x, relation[y][x])
        unhappy = set()
        for i in range(n):
            if i in unhappy:
                continue
            pi, rpi = pair[i]
            for j in range(n):
                if j == i or j == pi:
                    continue
                pj, rpj = pair[j]
                if relation[i][j] > rpi and relation[j][i] > rpj:
                    unhappy.add(i)
                    unhappy.add(j)
                    break
        
        #print(unhappy)
        return len(unhappy)