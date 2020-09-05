class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        if abs(locations[finish] - locations[start]) > fuel:
            return 0
        n = len(locations)
        #midpoints = []
        distances = [[0] * n for _ in range(n)]
        '''
        for i in range(n):
            if locations[i] > locations[finish]:
                l, r = locations[finish], locations[i]
            else:
                l, r = locations[i], locations[finish]
            ans = 0
            for j in range(n):
                if l < locations[j] < r:
                    ans += 1
            midpoints.append(ans)
        for i in range(n):
            for j in range(n):
                distances[i][j] = abs(locations[j]- locations[i])
        #print(midpoints)
        '''
        #print(distances)
        res = 0            
        @lru_cache(None)
        def helper(fuel, currpoint):
            if distances[currpoint][finish] > fuel:
                return 0
            count = 0
            if currpoint == finish:
                count += 1
            for i in range(n):
                if i == currpoint:
                    continue
                elif distances[currpoint][i] > fuel:
                    continue
                count += helper(fuel - distances[currpoint][i], i)
            return count % (10 ** 9 + 7)
                
                
            
        return helper(fuel, start)