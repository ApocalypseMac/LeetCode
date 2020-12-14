from collections import deque
class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        if n == 1:
            return 1
        weights = [0]
        p = 0
        for i in range(n):
            p += boxes[i][1]
            weights.append(p)
        ports = [0, 0]
        p1 = 0
        for i in range(1, n):
            if boxes[i][0] != boxes[i-1][0]:
                p1 += 1
            ports.append(p1)
        #print(weights, ports)
        queue = deque([]) # increasing queue
        dp = [0] * (n + 1)
        f = [0] * (n + 1)
        queue.append(0)
        for i in range(1, n + 1):
            while queue and (i - queue[0] > maxBoxes or weights[i] - weights[queue[0]] > maxWeight):
                queue.popleft()
            dp[i] = f[queue[0]] + ports[i] + 2
            if i != n:
                f[i] = dp[i] - ports[i+1]
                while queue and f[i] <= f[queue[-1]]:
                    queue.pop()
                queue.append(i)
            #print(queue)
        #print(dp, f)
        return dp[-1]
        
        
        