# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        begin2 = list2
        end2 = list2
        while end2.next:
            end2 = end2.next
        dummyhead = ListNode(None)
        dummyhead.next = list1
        end1 = dummyhead
        while a:
            a -= 1
            end1 = end1.next
        begin1 = list1
        while b:
            b -= 1
            begin1 = begin1.next
        end1.next = begin2
        end2.next = begin1.next
        return dummyhead.next