#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        dummyhead = ListNode(None)
        dummyhead.next = head
        start = dummyhead
        # start -> k nodes -> end
        while start:
            end = start.next
            count = k
            # count nodes
            while count and end:
                count -= 1
                end = end.next
            if count: # not have k nodes
                break
            # if enough, reverse (LC092)
            count1 = k
            curr = start.next
            while count1 > 1:
                node = curr.next
                curr.next = node.next
                node.next = start.next
                start.next = node
                count1 -= 1
            start = curr
        return dummyhead.next




# @lc code=end

