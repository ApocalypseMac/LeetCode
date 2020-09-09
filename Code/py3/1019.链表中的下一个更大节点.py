#
# @lc app=leetcode.cn id=1019 lang=python3
#
# [1019] 链表中的下一个更大节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        _listnode = []
        while head:
            _listnode.append(head.val)
            head = head.next
        n = len(_listnode)
        if n == 0:
            return []
        elif n == 1:
            return [0]
        _listnode.reverse()
        res = []
        stack = [float('INF')] # decreasing stack
        for num in _listnode:
            while num >= stack[-1]:
                stack.pop()
            if len(stack) == 1:
                res.append(0)
            else:
                res.append(stack[-1])
            stack.append(num)



        return res[::-1]
        
# @lc code=end

