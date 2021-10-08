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

def find_ancestors(root, node1, order):
    if root == None:
        return False
    order.append(root.data)
    if root.data == node1.data:
        return True
    if find_ancestors(root.left, node1, order) or find_ancestors(root.right, node1, order):
        return True
    order.pop()
    return False
    
def base(root, node1, node2):
    if root == None:
        return None
    order = []
    find_ancestors(root, node1, order)
    order1 = []
    find_ancestors(root, node2, order1)
    n1 = len(order)
    n2 = len(order1)
    i, j = 0, 0
    print(order, order1)
    ans = -1
    while i <= n1 - 1 and j <= n2 - 1:
        if order[i] == order[j]:
            ans = order[i]
        i += 1
        j += 1
    return ans

def func(root, node1, node2):
    if root == None:
        return None
    if root.data == node1.data:
        return node1.data
    elif root.data == node2.data:
        return node2.data

    left = func(root.left, node1, node2)
    right = func(root.right, node1, node2) 

    if left == node1.data and right == node2.data:
        return root.data
    elif left:
        return left
    elif right:
        return right   
    else:
        return None

print(base(root1, root1.left.left, root1.right))
print(func(root1, root1.left.left, root1.right))


