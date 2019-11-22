https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # decode l1
        l1_list = []
        while l1 is not None:
            l1_list.append(str(l1.val))
            l1=l1.next
        l1_list.reverse()
        num1 = "".join(l1_list)
        
        # decode l2
        l2_list = []
        while l2 is not None:
            l2_list.append(str(l2.val))
            l2=l2.next
        l2_list.reverse()
        num2 = "".join(l2_list)
        
        # add
        ans = int(num1)+int(num2)
        
        # encode answer
        ans_list = list(str(ans))
        ans_list.reverse()
        ans_ll = ListNode(ans_list[0])
        temp = ans_ll
        for each in ans_list[1:]:
            temp.next = ListNode(each)
            temp = temp.next
        return ans_ll
