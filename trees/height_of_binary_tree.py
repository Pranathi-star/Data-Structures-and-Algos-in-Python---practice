class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)

def heightbintree(root):
    if root == None:
        return 0
    elif root.left == None and root.right == None:
        return 0
    else:
        if root.left and root.right:
            return max(heightbintree(root.left), heightbintree(root.right)) + 1
        elif root.left:
            return heightbintree(root.left) + 1
        elif root.right:
            return heightbintree(root.right) + 1

print(heightbintree(root))