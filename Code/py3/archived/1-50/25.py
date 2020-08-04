# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummyhead = ListNode(None)
        dummyhead.next = head
        start, end = head, dummyhead
        flag = True
        while True:
            count = k 
            while count and end:
                end = end.next
                count -= 1
            if end is None:
                break
            if flag:
                dummyhead.next = end
                flag = False
            else:
                head.next = end
                head = start
            end = end.next
            prev = end
            curr = start
            while curr != end:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            start = head.next
            end = head
        
        return dummyhead.next