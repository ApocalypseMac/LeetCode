# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummyhead1 = ListNode(None)
        dummyhead2 = ListNode(None)
        curr1 = dummyhead1
        curr2 = dummyhead2
        while head:
            if head.val < x:
                curr1.next = head
                head = head.next
                curr1 = curr1.next
                curr1.next = None
            else:
                curr2.next = head
                head = head.next
                curr2 = curr2.next
                curr2.next = None
        curr1.next = dummyhead2.next
        return dummyhead1.next