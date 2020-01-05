# https://leetcode.com/problems/binary-tree-pruning
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        # in place recursion
        # check if root is none
        if root is not None:
            # recursion over left sub tree and right sub tree
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
            # our condition where root is 0 and both left and right are none
            # this is true when we move to the previous step(step out of the recursion) where the below elements become none
            if root.val ==0 and root.left == root.right == None:
                # return None as root
                return None
            # return root
            return root
