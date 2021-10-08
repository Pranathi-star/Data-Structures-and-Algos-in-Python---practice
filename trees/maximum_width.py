from collections import deque

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

def max_width(root, new_idx):
    if root == None:
        return
    queue = deque()
    queue.append([root, -1])
    while len(queue):
        for _ in range(len(queue)):
            curr_node, parent_lvl = queue.popleft()
            curr_node.data = 6
            new_idx += 1
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
    

            


print(max_width(root, new_index = 0))