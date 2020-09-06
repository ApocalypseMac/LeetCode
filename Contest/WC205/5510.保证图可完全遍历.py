class Solution:
    from collections import deque
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edgeA = [set() for _ in range(n + 1)] # Edges Alice can walk through
        edgeB = [set() for _ in range(n + 1)] # Edges Bob can walk through
        edgeP = [set() for _ in range(n + 1)] # Public edges
        for edge in edges:
            u, v = edge[1], edge[2]
            if edge[0] == 1:
                edgeA[u].add(v)
                edgeA[v].add(u)
            elif edge[0] == 2:
                edgeB[u].add(v)
                edgeB[v].add(u)
            else:
                edgeA[u].add(v)
                edgeA[v].add(u)
                edgeB[u].add(v)
                edgeB[v].add(u)
                edgeP[u].add(v)
                edgeP[v].add(u)
                
        def connected(edgex): # BFS, whether A or B can traverse all nodes
            visited = [False] * (n + 1)
            visited[0] = True
            visited[1] = True
            queue = deque([1])
            while queue:
                curr = queue.popleft()
                for v in edgex[curr]:
                    if visited[v] is False:
                        queue.append(v)
                        visited[v] = True
            return all(visited)
        
        if connected(edgeA) is False or connected(edgeB) is False:
            return -1
        
        npart = 0 # number of connected components by public edges
        visited = [False] * (n + 1)
        visited[0] = True
        for i in range(n + 1):
            if visited[i]:
                continue
            else:
                npart += 1
                visited[i] = True
                queue = deque([i])
                while queue:
                    curr = queue.popleft()
                    for v in edgeP[curr]:
                        if visited[v] is False:
                            queue.append(v)
                            visited[v] = True
        
        # greedy deletion
        # the number of edges left is num(A_spantree) + num(B_spantree) - num(Public_spantrees) (calculated twice)
        # num(Public_spantrees) = num(vertices) (n) - num(conn_components)
        # since A and B can traverse the graph, num(A_spantree) = num(B_spantree) = n - 1
        return len(edges) - 2 * (n - 1) + n - npart
                
            
                