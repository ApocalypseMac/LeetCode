# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        def isValidEven(vals):
            n = len(vals)
            for i in range(n):
                if vals[i] & 1:
                    return False
            for i in range(n-1):
                if vals[i] <= vals[i+1]:
                    return False
            return True
        
        def isValidOdd(vals):
            n = len(vals)
            for i in range(n):
                if vals[i] & 1 == 0:
                    return False
            for i in range(n-1):
                if vals[i] >= vals[i+1]:
                    return False
            return True
            
        queue = deque([root])
        depth = 0
        while queue:
            depth += 1
            n = len(queue)
            vals = []
            for i in range(n):
                curr = queue.popleft()
                vals.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if depth & 1:
                if isValidOdd(vals) is False:
                    return False
            else:
                if isValidEven(vals) is False:
                    return False
        return True