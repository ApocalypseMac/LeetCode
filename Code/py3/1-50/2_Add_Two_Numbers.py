# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        curr = result
        carry = 0
        while l1 is not None or l2 is not None:
            x = carry
            if l1 is None:
                x += 0
            else:
                x += l1.val
                l1 = l1.next
            if l2 is None:
                x += 0
            else:
                x += l2.val
                l2 = l2.next 
            curr.next = ListNode(x % 10)
            carry = x // 10
            curr = curr.next
        if carry > 0:
            curr.next = ListNode(carry)
        return result.next