class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class Solution:
    def __init__(self):
        self.res = float('-inf')

    def max_cost_path(self, root):
        if root == None:
            return 0
        lv = self.max_cost_path(root.left)
        rv = self.max_cost_path(root.right)
        self.res = max(self.res, lv+rv+root.data)
        return root.data + max(lv, rv)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)

tree1 = Solution()
tree1.max_cost_path(root)
print(tree1.res)
