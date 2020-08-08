#
# @lc app=leetcode.cn id=968 lang=python3
#
# [968] 监控二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # states
        # 0: not covered
        # 1: covered
        # 2: installed
        def helper(node):
            if node is None:
                return 0, 0, 10000
            l = helper(node.left)
            r = helper(node.right)
            
            dp0 = l[1] + r[1]
            dp1 = min(l[1] + r[2], l[2] + r[1], l[2] + r[2])
            dp2 = min(l) + min(r) + 1            
            return dp0, dp1, dp2

        return min(helper(root)[1:])
        
# @lc code=end

