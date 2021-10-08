class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []
    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        self.res.append(root.data)
        self.inorder(root.right)
        return

    def preorder(self, root):
        if root == None:
            return
        self.res.append(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
    
    def postorder(self, root):
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        self.res.append(root.data)

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.right = TreeNode(5)
root.left.right = TreeNode(2)
tree1 = Solution()
tree1.inorder(root)
print(tree1.res)




        