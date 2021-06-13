from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

order = []

def level_order(root):
    if root == None:
        return
    queue = deque()
    queue.append(root)
    while(len(queue) > 0):
        current_node = queue.popleft()
        order.append(current_node.data)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

level_order(root)
print(order)

