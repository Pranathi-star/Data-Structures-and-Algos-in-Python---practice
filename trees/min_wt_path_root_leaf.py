class TreeNode:
    def __init__(self, val, weight):
        self.val = val
        self.left = None
        self.right = None
        self.weight = weight

root = TreeNode(1, 0)
root.left = TreeNode(2, 4)
root.right = TreeNode(3, 6)
root.left.left = TreeNode(4, 1)
root.left.right = TreeNode(5, 1)
root.right.left = TreeNode(6, 3)
root.right.right = TreeNode(7, 0)

def min_weight_path(root):
    if root == None:
        return 0
    elif root.left == None and root.right == None:
        return root.weight
    else:
        if root.left and root.right:
            return min(min_weight_path(root.left), min_weight_path(root.right)) + root.weight
        elif root.left:
            return min_weight_path(root.left) + root.weight
        elif root.right:
            return min_weight_path(root.right) + root.weight

print(min_weight_path(root))