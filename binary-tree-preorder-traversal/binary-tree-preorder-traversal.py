# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder_util(self, root, res):
        if root:
            res.append(root.val)
            self.preorder_util(root.left, res)
            self.preorder_util(root.right, res)
        return res
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        return self.preorder_util(root, res)
            
        