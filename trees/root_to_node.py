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

order = []

def root_to_node(root, node):
    if root == None:
        return False
    order.append(root.data)
    if root.data == node.data:
        return True
    if root_to_node(root.left, node) or root_to_node(root.right, node):
        return True
    order.pop()
    return False

def base(root, node):
    if root == None:
        return order
    root_to_node(root, node)
    return order


print(base(root1, root1.left.left))