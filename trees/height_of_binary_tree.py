class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

# constructing a tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)

def height_of_binary_tree(root):
    if (root and root.left == None and root.right == 0) or root == None:
        return 0
    height1 = 0
    height2 = 0
    if root.left:
        height1 = height_of_binary_tree(root.left) + 1
    if root.right:
        height2 = height_of_binary_tree(root.right) + 1
    return max(height1, height2)

print(height_of_binary_tree(root))