# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Inorder -> Find Decreasing Pair
        curr = root
        stack = []
        prev = TreeNode(-2147483649) # -2 ** 31 - 1
        decreasing = [] # decreasing pair
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            if prev.val > node.val:
                decreasing.append((prev, node))
            if node.right:
                curr = node.right
            prev = node
        if len(decreasing) == 1: # one pair: swap [0][0] and [0][1]
            decreasing[0][0].val, decreasing[0][1].val = decreasing[0][1].val, decreasing[0][0].val
        else: # two pair: swap [0][0] and [1][1]
            decreasing[0][0].val, decreasing[1][1].val = decreasing[1][1].val, decreasing[0][0].val