# https://leetcode.com/problems/univalued-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.set_d = set()
        
    def traversal(self, root):
        if root is not None:
            self.set_d.add(root.val)
            return self.traversal(root.left), self.traversal(root.right)
        else:
            return None
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.traversal(root)
        print(self.set_d)
        if len(self.set_d) != 1:
            return False
        else:
            return True
                    
                
