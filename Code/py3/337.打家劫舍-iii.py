#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        # dp 0: not rob 1: rob
        def dfs(root):
            if root is None:
                return [0, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            ans = [0] * 2
            ans[1] = root.val + left[0] + right[0]
            ans[0] = max(left) + max(right)
            return ans
        return max(dfs(root))
        
# @lc code=end

