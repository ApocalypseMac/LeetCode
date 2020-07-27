# Leetcode Tree Problems

---

## Traversal (Binary Tree)

 1. **Preorder (144)**
 [Mid, Left, Right] 
- Recursion:

        [Mid, Left, Right] 
            
            def preorderTraversal(self, root: TreeNode) -> List[int]:
                if root is None:
                    return []
                return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
            
- Iteration

        Stack
        
            def preorderTraversal(self, root: TreeNode) -> List[int]:
                if root is None:
                    return []
                result = []
                stack = [root]
                while stack:
                    curr = stack.pop()
                    result.append(curr.val)
                    if curr.right: # push right then left
                        stack.append(curr.right)
                    if curr.left:
                        stack.append(curr.left)
                return result

 2. **Inorder (94)**
  [Left, Mid, Right] 
- Recursion:

        [Left, Mid, Right] 
            
            def inorderTraversal(self, root: TreeNode) -> List[int]:
                if root is None:
                    return []
                return self.preorderTraversal(root.left) + [root.val] + self.preorderTraversal(root.right)
            
- Iteration

        Stack
        
            def inorderTraversal(self, root: TreeNode) -> List[int]:    
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

 3. **Postorder (145)**
 [Left, Right, Mid]
- Recursion:

        [Left, Right, Mid]
            
            def postorderTraversal(self, root: TreeNode) -> List[int]:
                if root is None:
                    return []
                return self.preorderTraversal(root.left) + self.preorderTraversal(root.right)+ [root.val] 
            
- Iteration

        Stack ([Mid, Right, Left][::-1])
        
            def postorderTraversal(self, root: TreeNode) -> List[int]:    
                if root is None:
                    return []
                result = []
                stack = [root]
                while stack:
                    curr = stack.pop()
                    result.append(curr.val)
                    if curr.left:
                        stack.append(curr.left)
                    if curr.right:
                        stack.append(curr.right)
                return result[::-1]


        Stack ([left, right, mid])
        
            def postorderTraversal(self, root: TreeNode) -> List[int]:    
                if root is None:
                    return []
                result = []
                stack = [root]
                curr = root # NOT None ([1,2] will fail)
                while stack:
                    peek = stack[-1]
                    if peek.left and curr != peek.left and curr != peek.right:
                        curr = peek.left
                        stack.append(curr)
                    elif peek.right and curr != peek.right:
                        curr = peek.right
                        stack.append(curr)
                    else:
                        curr = stack.pop()
                        result.append(curr.val)
                return result
 4. **Level Order (102)**
- Recursion
        DFS + depth info
        
            def levelOrder(self, root: TreeNode) -> List[List[int]]:    
                if root is None:
                    return []
                levels = []
        
                def recur(node, level):
                    if len(levels) == level:
                        levels.append([])
                    levels[level].append(node.val)
                    if node.left:
                        recur(node.left, level + 1)
                    if node.right:
                        recur(node.right, level + 1)
                recur(root, 0)
                return levels
- Iteration
        Queue
        
            def levelOrder(self, root: TreeNode) -> List[List[int]]:    
                if root is None:
                    return []
                level = 0
                levels = []
                queue = [root]
                while queue:
                    levels.append([])
                    length = len(queue)
                    for i in range(length):
                        curr = queue.pop(0)
                        levels[level].append(curr.val)
                        if curr.left:
                            queue.append(curr.left)
                        if curr.right:
                            queue.append(curr.right)
                    level += 1
                return levels



## Hints of Problems
- **94. Binary Tree Inorder Traversal** *Mid* 
    - Recursion / Iteration.
- **96. Unique Binary Search Trees** *Mid* 
    - Catalan Number $G(n) = G(0)G(n-1)+G(1)G(n-2)+\ldots +G(n-1)G(0)$.
- **95. Unique Binary Search Trees II** *Mid* 
    - Recursion: Consider generating tree from [start, end], return list of possible trees. Loop over value of root and combine corresponding list of left subtree(s) and right subtree(s).
- **98. Validate Binary Search Tree** *Mid* 
    - Traverse (inorder) then validate sorted / Validate during traversal.
    - *How to deal with the first value.*
- **99. Recover Binary Search Tree** *Hard*
    - Traverse (inorder) and track decreasing pair (prev < curr).
    - *One pair / Two pairs.*
- **100. Same Tree** *Easy*
    - Recursion (Preorder).
- **101. Symmetric Tree** *Easy*
    - Recursion (Preorder) / Iteration (BFS Queue).
- **102. Binary Tree Level Order Traversal** *Mid*
    - Recursion (DFS + depth) / Iteration.
- **103. Binary Tree Zigzag Level Order Traversal** *Mid*
    - BFS.
- **104. Maximum Depth of Binary Tree** *Easy*
    - Recursion / DFS / BFS.
- **105. Construct Binary Tree from Preorder and Inorder Traversal** *Mid*
    - Recursion.
    - *buildTree(prel, prer, inl, inr).*
    - *First element in pre is root.*
- **106. Construct Binary Tree from Inorder and Postorder Traversal** *Mid*
    - Recursion.
    - *buildTree(inl, inr, postl, postr).*
    - *Last element in post is root.*
- **107. Binary Tree Level Order Traversal II** *Easy*
    - BFS + reverse level order.
- **108. Convert Sorted Array to Binary Search Tree** *Easy*
    - Recursion.
    - *Height balanced -> Middle element is value of root.*
- **110. Balanced Binary Tree** *Easy*
    - Recursion (Postorder).
    - *return height if balanced else -1.*
- **111. Minimum Depth of Binary Tree** *Easy*
    - Recursion / DFS / BFS (similar with 104).
    - *stop if larger than minimum value.*
- **112. Path Sum** *Easy*
    - Recursion.
- **113. Path Sum II** *Mid*
    - Recursion.
    - *Add parameter to store path.*
- **114. Flatten Binary Tree to Linked List** *Mid*
    - Preorder / top-to-bottom / Recursion (Postorder).
- **116. Populating Next Right Pointers in Each Node** *Mid*
    - BFS (Level order).
    - *Queue: O(N) / Using next pointers of previous level: O(1).*
- **117. Populating Next Right Pointers in Each Node II** *Mid*
    - BFS (Level order).
    - *Queue: O(N) / Using next pointers of previous level: O(1).*
    - *Mark the head of each level.*
- **124. Binary Tree Maximum Path Sum** *Hard*
    - Recursion (bottom-to-top).
    - *Calculate leftmax (0 if negative) and rightmax and compare with maxval.*
    - *return root.val + max(leftmax, rightmax).*
- **129. Sum Root to Leaf Numbers** *Mid*
    - Recursion.
    - *Add parameter to store path.*
- **144. Binary Tree Preorder Traversal** *Mid*
    - Recursion / Iteration.
- **145. Binary Tree Postorder Traversal** *Hard*
    - Recursion / Iteration.
- **173. Binary Search Tree Iterator** *Mid*
    - Inorder traversal.
- **199. Binary Tree Right Side View** *Mid*
    - BFS.
- **222. Count Complete Tree Nodes** *Mid*
    - Determine level -> Binary Search 
- **226. Invert Binary Tree** *Easy*
    - Recursion / Iteration (Queue).
- **230. Kth Smallest Element in a BST** *Mid*
    - Inorder traversal.
- **235. Lowest Common Ancestor of a Binary Search Tree** *Easy*
    - Recursion (top-to-bottom) / Loop.
    - *Judge by value*
- **236. Lowest Common Ancestor of a Binary Tree** *Mid*
    - Memorize Path (Recursion / Iteration) / Parent Node Map / Inorder + Index Map (similar with 235) / Recursion.
- **250. Count Univalue Subtrees** *Mid*
    - Recursion (bottom-to-top).
- **255. Verify Preorder Sequence in Binary Search Tree** *Mid*
    - Recursion (*TLE*) / Iteration (Simulate Preorder Process).
- **257. Binary Tree Paths** *Easy*
    - Recursion (top-to-bottom).
- **270. Closest Binary Search Tree Value** *Easy*
    - Loop + Store minimum.
- **272. Closest Binary Search Tree Value II** *Hard*
    - Inorder traversal (*O(n)*) / Parent map + Pred/Succ + Merge (*O(max(k, log(n))*). 
- **285. Inorder Successor in BST** *Mid*
    - Inorder / Parent map (272/510).
- **297. Serialize and Deserialize Binary Tree**
    - Traversal (Preorder / Levelorder / ...).
    - *Add some NULL nodes.*
- **298. Binary Tree Longest Consecutive Sequence** *Mid*
    - Recursion (top-to-bottom).
- **333. Largest BST Subtree** *Mid*
    - Recursion (bottom-to-top) + BST hashmap (smallest/largest val).
- **337. House Robber III** *Mid*
    - DP (two state) + Recursion (bottom-to-top).
- **366. Find Leaves of Binary Tree** *Mid*
    - Recursion (bottom-to-top) + Level hashmap (or directly add to result in recursion process).
- **404. Sum of Left Leaves** *Easy*
    - Recursion (top-to-bottom) / Iteration.
    - *Traverse and calculate.*
- **426. Convert Binary Search Tree to Sorted Doubly Linked List** *Mid*
    - Inorder traversal.
    - *Need a dummyhead.*
- **428. Serialize and Deserialize N-ary Tree** *Hard*
    - Traversal (Preorder / Levelorder / ...).
    - *Add some NULL nodes.*
- **429. N-ary Tree Level Order Traversal** *Mid*
    - Similar with 102. 
- **431. Encode N-ary Tree to Binary Tree** *Hard*
    - Levelorder traversal
    - *Left subtree as children, right subtree as same parent*
    - 





