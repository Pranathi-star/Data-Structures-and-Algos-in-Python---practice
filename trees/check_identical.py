class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.left.right.left = TreeNode(6)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.left.right.left = TreeNode(6)

def check_identical(root1, root2):
    if root1 == None and root2 == None:
        return True
    elif (root1 == None and root2 != None) or (root1 != None and root2 == None):
        return False
    elif root1.data != root2.data:
            return False
    else:
        return check_identical(root1.left, root2.left) and check_identical(root1.right, root2.right)

print(check_identical(root1, root2))