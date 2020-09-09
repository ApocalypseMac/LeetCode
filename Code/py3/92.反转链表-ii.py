#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummyhead = ListNode(None)
        dummyhead.next = head
        prev = dummyhead
        while m > 1:
            m -= 1
            n -= 1
            prev = prev.next
        curr = prev.next
        while n > 1:
            node = curr.next
            curr.next = node.next
            node.next = prev.next
            prev.next = node
            n -= 1
        return dummyhead.next



# @lc code=end

