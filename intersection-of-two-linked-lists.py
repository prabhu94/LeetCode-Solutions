# https://leetcode.com/problems/intersection-of-two-linked-lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = 0
        lenB = 0
        tempA = headA
        tempB = headB
        if tempA is not None and tempB is not None:
            while tempA is not None:
                tempA = tempA.next
                lenA +=1
                
            while tempB is not None:
                tempB = tempB.next
                lenB +=1
                
        tempA = headA
        tempB = headB
        if tempA is not None and tempB is not None:
            if lenA >= lenB:
                i=0
                while i < lenA-lenB:
                    tempA = tempA.next
                    i+=1
                
            if lenA < lenB:
                i=0
                while i< lenB-lenA:
                    print(i)
                    tempB = tempB.next
                    i+=1
                
            while tempA is not None:
                if tempA == tempB :
                    return tempA
                
                tempA=tempA.next
                tempB=tempB.next
                
