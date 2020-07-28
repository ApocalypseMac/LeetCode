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
        count = m
        while count > 1:
            prev = prev.next
            count -= 1
        curr = prev.next
        count = n
        while count > m:
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
            count -= 1
        return dummyhead.next