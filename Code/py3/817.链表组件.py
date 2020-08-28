#
# @lc app=leetcode.cn id=817 lang=python3
#
# [817] 链表组件
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        G = set(G)
        prev = False # prev in G
        node = head
        res = 0
        while node:
            if node.val in G:
                curr = True
                if prev is False:
                    res += 1
            else:
                curr = False
            prev = curr
            node = node.next
        return res


        
# @lc code=end

