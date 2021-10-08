class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.left = TreeNode(4)
root1.right.right = TreeNode(4)

def check_symmetry(left, right):
    if left == None and right == None:
        return True
    elif (left == None and right != None) or (left != None and right == None):
        return False
    elif left.data != right.data:
            return False
    else:
        return (check_symmetry(left.left, right.right)) and (check_symmetry(left.right, right.left))

print(root1 == None or check_symmetry(root1.left, root1.right))