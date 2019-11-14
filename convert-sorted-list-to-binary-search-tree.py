# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):            
    
    def build(self,lst):
        if len(lst)>0:
            mid = (len(lst)) / 2
            root = TreeNode(lst[mid]) 
            root.left = self.build(lst[:mid])
            root.right = self.build(lst[mid+1:])
            return root
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        sort_list = []
        while head is not None:
            sort_list.append(head.val)
            head= head.next
        
        print(sort_list)
        return self.build(sort_list)
        
