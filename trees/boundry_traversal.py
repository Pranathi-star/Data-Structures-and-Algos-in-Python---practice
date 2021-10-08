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

def check_leaf(curr_node):
    return True if curr_node.left == None and curr_node.right == None else False

def get_leaves(root):
    if root == None:
        return
    if check_leaf(root):
        order.append(root.data)
        return
    if root.left:
        get_leaves(root.left)
    if root.right:
        get_leaves(root.right)
    

def left_boundry(root):
    curr_node = root.left
    while curr_node:
        if not check_leaf(curr_node):
            order.append(curr_node.data)
            if curr_node.left:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        else:
            break

def right_boundry(root):
    curr_node = root.right
    stack = []
    while curr_node:
        if not check_leaf(curr_node):
            stack.append(curr_node.data)
        if curr_node.right:
            curr_node = curr_node.right
        else:
            curr_node = curr_node.left
    
    while len(stack):
        order.append(stack.pop())

if not check_leaf(root):
    order.append(root.data)
left_boundry(root)
get_leaves(root)
right_boundry(root)
print(order)

