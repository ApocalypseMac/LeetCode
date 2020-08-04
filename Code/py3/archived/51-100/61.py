# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head
        length = 0
        dummyhead = ListNode(None)
        dummyhead.next = head
        tail = dummyhead
        while tail.next:
            tail = tail.next
            length += 1
        shift = k % length
        if shift == 0:
            return head
        count = length - shift
        newtail = dummyhead
        while count:
            newtail = newtail.next
            count -= 1
        dummyhead.next = newtail.next
        tail.next = head
        newtail.next = None
        return dummyhead.next