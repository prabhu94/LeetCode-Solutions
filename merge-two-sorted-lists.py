# https://leetcode.com/problems/merge-two-sorted-lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp_list = []
        # get lengths
        tl1 = l1
        tl2 = l2
        ll1 =[]
        ll2=[]
        while tl1 is not None:
            ll1.append(tl1.val)
            tl1 = tl1.next
        while tl2 is not None:
            ll2.append(tl2.val)
            tl2 = tl2.next
        
        if len(ll1)>=len(ll2):
            while l1 is not None:
                temp_list.append(l1.val)
                if l2 is not None:
                    temp_list.append(l2.val)
                    l2 = l2.next
                l1 = l1.next
        else:
            while l2 is not None:
                temp_list.append(l2.val)
                if l1 is not None:
                    temp_list.append(l1.val)
                    l1 = l1.next
                l2= l2.next
        temp_list = sorted(temp_list)
        if len(temp_list)>0:
            new_ln = ListNode(temp_list[0])
            temp_ln = new_ln
            for each in temp_list[1:]:
                temp_ln.next = ListNode(each)
                temp_ln = temp_ln.next
            return(new_ln)
                
