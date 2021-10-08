class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class Solution:
    def check_balanced(self, root):
        if root == None:
            return 0
        lh = self.check_balanced(root.left)
        if lh == -1: return -1

        rh = self.check_balanced(root.right)
        if rh == -1: return -1

        if abs(rh - lh) > 1:
            return -1
        else:
            return max(lh, rh) + 1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

tree1 = Solution()
print(tree1.check_balanced(root) != -1)
