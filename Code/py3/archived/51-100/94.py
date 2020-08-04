# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # Recursion ([left, mid, right])
        '''
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        '''

        # Stack ([left, mid, right])
        if root is None:
            return []
        result = []
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop() # must set a new pointer
            result.append(node.val)
            if node.right:
                curr = node.right
        return result