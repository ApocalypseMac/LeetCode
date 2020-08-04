# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        dummyhead = ListNode(None)
        dummyhead.next = head
        prev = dummyhead
        curr1, curr2 = head, head
        while curr1 and curr1.next:
            curr2 = curr1.next
            prev.next = curr2
            curr1.next = curr2.next
            curr2.next = curr1
            prev = curr1
            curr1 = curr1.next
            
        return dummyhead.next