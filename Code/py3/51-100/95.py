# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # generate tree from [start, end]
        if n == 0:
            return []
        def generateFromRange(start, end) -> List[TreeNode]:
            if start > end:
                return [None]
            #elif start == end:
            #    return [TreeNode(start)]
            else:
                treelist = []
                for num in range(start, end + 1):
                    llist = generateFromRange(start, num - 1)
                    rlist = generateFromRange(num + 1, end)
                    for l in llist:
                        for r in rlist:
                            root = TreeNode(num)
                            root.left = l
                            root.right = r
                            treelist.append(root)
                return treelist
        return generateFromRange(1, n)