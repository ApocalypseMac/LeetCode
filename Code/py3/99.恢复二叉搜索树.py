#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = TreeNode(-2147483649)
        stack = []
        curr = root
        decpairs = []
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            if node.val < prev.val:
                decpairs.append((prev, node))
            prev = node
            if node.right:
                curr = node.right
        if len(decpairs) == 1:
            decpairs[0][0].val, decpairs[0][1].val = decpairs[0][1].val, decpairs[0][0].val
        else:
            decpairs[0][0].val, decpairs[1][1].val = decpairs[1][1].val, decpairs[0][0].val

            
        
        
        
# @lc code=end

