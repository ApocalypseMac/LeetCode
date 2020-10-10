# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter
class Solution:
    def navigation(self, root: TreeNode) -> int:
        # a method for general tree graph
        edges = []

        # tree to adjacent table
        def helper(root, parent):
            if root is None:
                return 
            while len(edges) <= root.val:
                edges.append(set())
            if parent:
                edges[parent].add(root.val)
                edges[root.val].add(parent)
            helper(root.left, root.val)
            helper(root.right, root.val)
            return
        
        helper(root, 0)

        n = len(edges) - 1
        
        # eliminate nodes with degree = 2 (no bifurcation, not leaf node)
        for i in range(1, n + 1):
            if len(edges[i]) == 2:
                a, b = list(edges[i])
                edges[i] = set()
                edges[a].remove(i)
                edges[b].remove(i)
                edges[a].add(b)
                edges[b].add(a)

        count = Counter()
        res = 0
        # count each 3-node's adjacent leaf node number 
        # if adjacent to 2 leaf nodes, need install camera in one of them
        # if 3 leaf nodes (example 2), need install 2 cameras
        # easy to generate to general tree (with more degrees)
        # can verify from bottom to top (?)
        for i in range(1, n + 1):
            if len(edges[i]) == 1:
                neighbour = edges[i].pop()
                count[neighbour] += 1
                if count[neighbour] > 1:
                    res += 1
        return max(1, res) # at least 1 (if a chain: 1)