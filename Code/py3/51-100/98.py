# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Recursion
    '''
    def __init__(self):
        self.prev = - 2**100
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if self.isValidBST(root.left):
            if self.prev < root.val:
                self.prev = root.val
                return self.isValidBST(root.right)
        return False
    '''
    # In order traversal
    def isValidBST(self, root: TreeNode) -> bool:
        nums = self.inOrderTraversal(root)
        #print(nums)
        if len(nums) <= 1:
            return True
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                return False
        return True
    def inOrderTraversal(self, root):
        # Recursion
        '''
        if root is None:
            return []
        return self.inOrderTraversal(root.left) + [root.val] + self.inOrderTraversal(root.right)
        '''
        # Iteration
        if root is None:
            return []
        result = []
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            result.append(node.val)
            if node.right:
                curr = node.right
        return result