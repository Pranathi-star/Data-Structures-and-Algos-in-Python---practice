class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.left = TreeNode(2)
root1.right.right = TreeNode(4)

def func(root, res, curr_res, search_value, dir):
    if root == None:
        return
    if root.data == search_value:
        curr_res += 1
    else:
        curr_res = 1
        search_value = root.data

    res = max(curr_res, res)
    if root.left.data == search_value:
        pass

    

def main(root):
    if root == None:
        return 0
    res = 0
    res1 = 0
    func(root, res, curr_res = 0, search_value = root.data, dir = 0)
    func(root, res1, curr_res = 0, search_value = root.data, dir = 1)

    print(max(res, res1))

