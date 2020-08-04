# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyhead = ListNode(None)
        dummyhead.next = head
        fast = dummyhead
        slow = dummyhead
        while n >= 0:
            fast = fast.next
            n -= 1
            '''
            if fast == None and n >= 0:
                return head
            '''
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummyhead.next