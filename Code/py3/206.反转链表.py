#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # recursion
        '''
        if head is None or head.next is None:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node
        '''
        # iteration
        prev = None
        curr = head
        while curr:
            node = curr.next
            curr.next = prev
            prev = curr
            curr = node
        return prev
# @lc code=end

