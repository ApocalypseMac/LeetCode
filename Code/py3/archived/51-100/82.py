# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        dummyhead = ListNode(None)
        dummyhead.next = head
        slow, fast = dummyhead, head
        while fast.next:
            if fast.next.val != fast.val:
                if slow.next == fast:
                    slow = slow.next
                else:
                    slow.next = fast.next
            fast = fast.next

        if slow.next == fast:    
            slow.next = fast
        else:
            slow.next = None
        return dummyhead.next