#https://leetcode.com/problems/reverse-linked-listhttps://github.com/prabhu94/LeetCode-Solutions
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
        
    def reverseList(self, head: ListNode) -> ListNode:
        
        #define previous and current
        previous = None
        current = head
        
        while current is not None:
            
            # the next node is the one after current
            next = current.next
            
            # next node is the previous node (reverse)
            current.next = previous
            
            # prev is the next node
            previous = current
            
            # current is next node to move the iteration forward
            current = next
            
        return previous
            
            
