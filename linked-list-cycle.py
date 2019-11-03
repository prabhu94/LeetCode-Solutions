#https://leetcode.com/problems/linked-list-cycle
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen_nodes = []
        while (head != None):
            if head in seen_nodes:
                return True
            else:
                seen_nodes.append(head)
            head = head.next
        return False
