# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        cnt = 0
        curr = head
        while curr:
            curr = curr.next
            cnt += 1
        dummyhead = ListNode(0)
        dummyhead.next = head
        start = k
        end = cnt + 1 - k
        s = dummyhead
        while start:
            s = s.next
            start -= 1
        e = dummyhead
        while end:
            e = e.next
            end -= 1
        s.val, e.val = e.val, s.val
        return dummyhead.next