class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class Solution:
    def __init__(self):
        self.res = float('-inf')

    def find_diameter(self, root):
        if root == None:
            return 0
        lh = self.find_diameter(root.left)
        rh = self.find_diameter(root.right)
        self.res = max(self.res, lh+rh)
        return max(lh, rh) + 1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)

tree1 = Solution()
tree1.find_diameter(root)
print(tree1.res)
