from sortedcontainers import SortedList
class BlackBox:
    # NOTE: direction -1 -> 0 for convenience
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.number = 2 * (m + n)
        self.corners = {0: (0, ), self.m: (1, ), self.m + self.n: (0, ), 2 * self.m + self.n: (1, )}
        self.routes = [] # store each route (by point and direction), each route is a list
        self.whichroute = dict() # (point, direction) -> (index in self.routes, index in spec route)
        self.holes = [] # holes of each route, stored as sortedlist
        self.opened = set() # opened holes, store in rind (route index) form
        self._preprocess()
        #print(self.routes)
        #print(self.whichroute)


    def _nextindex(self, index, direction):
        if direction == 1:
            newindex = (self.number - index) % self.number
        else:
            newindex = (2 * self.m - index) % self.number
        if newindex in self.corners: # not reverse
            return (newindex, direction)
        else: # reverse
            return (newindex, 1 - direction)


    def _preprocess(self):
        visited = [[False, False] for _ in range(self.number)]
        routenum = 0
        for i in range(self.number):
            if i in self.corners:
                dirs = self.corners[i]
            else:
                dirs = (0, 1)
            for d in dirs:
                if visited[i][d]:
                    continue
                route = [(i, d)]
                self.whichroute[(i, d)] = (routenum, 0)
                visited[i][d] = True

                routelen = 0
                while True:
                    nexti, nextd = self._nextindex(i, d)
                    if visited[nexti][nextd]: # find loop
                        break
                    routelen += 1
                    route.append((nexti, nextd))
                    self.whichroute[(nexti, nextd)] = (routenum, routelen)
                    visited[nexti][nextd] = True
                    i, d = nexti, nextd
                self.routes.append(route)
                routenum += 1
        for i in range(routenum):
            self.holes.append(SortedList([]))
        return
                    

    def open(self, index: int, direction: int) -> int:
        if direction == -1:
            direction = 0
        if index not in self.opened: # add to holes
            self.opened.add(index)
            if index in self.corners:
                dirs = self.corners[index]
            else:
                dirs = (0, 1)
            for d in dirs:
                rnum_, rind_ = self.whichroute[(index, d)]
                self.holes[rnum_].add(rind_)
        rnum, rind = self.whichroute[(index, direction)]
        h = self.holes[rnum]
        pos = h.bisect_right(rind) # search for next hole
        if pos == len(h):
            pos = 0
        #print(self.holes)
        return self.routes[rnum][h[pos]][0]


    def close(self, index: int) -> None:
        self.opened.remove(index)
        if index in self.corners:
            dirs = self.corners[index]
        else:
            dirs = (0, 1)
        for d in dirs:
            rnum, rind = self.whichroute[(index, d)]
            self.holes[rnum].remove(rind)
        #print(self.holes)
        return 

    '''old way
    def _indexToXY(self, index):
        if index <= self.m:
            return (index, self.n)
        elif index <= self.m + self.n:
            return (self.m, self.m + self.n - index)
        elif index <= 2 * self.m + self.n:
            return (2 * self.m + self.n - index, 0)
        else:
            return (0, index - 2 * self.m - self.n)
    
    def _xyToIndex(self, x, y):
        if y == self.n:
            return x
        elif x == self.m:
            return self.m + self.n - y
        elif y == 0:
            return 2 * self.m + self.n - x
        else:
            return 2 * self.m + self.n + y
    
    def _nextindex(self, index, direction):
        if direction == 1: # y = x + b
            b = y - x # bias
            x1, x2 = self.n - b, -b # intersection with top(y=n)/bottom(y=0)
            y1, y2 = b, self.m + b # intersection with left(x=0)/right(x=m)
            if 0 <= x1 <= self.m and x1 != x:
                newx, newy = x1, n
            elif 0 <= x2 <= self.m and x2 != x:
                newx, newy = x2, 0
            elif 0 <= y1 <= self.n and y1 != y:
                newx, newy = 0, y1
            else 0 <= y2 <= self.n and y2 != y:
                newx, newy = m, y2
        else: # y = -x + b
            b = x + y1
            x1, x2 = b - self.n, b # intersection with top(y=n)/bottom(y=0)
            y1, y2 = b, b - self.m # intersection with left(x=0)/right(x=m)
            if 0 <= x1 <= self.m and x1 != x:
                newx, newy = x1, n
            elif 0 <= x2 <= self.m and x2 != x:
                newx, newy = x2, 0
            elif 0 <= y1 <= self.n and y1 != y:
                newx, newy = 0, y1
            else 0 <= y2 <= self.n and y2 != y:
                newx, newy = m, y2
        newindex = self._xyToIndex(newx, newy)
        if newindex in self.corners: # not reverse
            return (newindex, direction)
        else: # reverse
            return (newindex, -direction)
    '''
        
# Your BlackBox object will be instantiated and called as such:
# obj = BlackBox(n, m)
# param_1 = obj.open(index,direction)
# obj.close(index)