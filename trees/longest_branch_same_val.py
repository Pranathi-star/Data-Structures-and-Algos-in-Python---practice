class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

root1 = TreeNode(2)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.left = TreeNode(2)
root1.right.right = TreeNode(4)

def length(node, ans):
    if (not node):
        return 0
    
  # Recursive calls to check for subtrees
    left = length(node.left, ans)
    right = length(node.right, ans)

    # Variables to store maximum lengths
    # in two directions
    Leftmax = 0
    Rightmax = 0

    # If curr node and it's left child has same value
    if (node.left and node.left.val == node.val): 
        Leftmax += left + 1 

    # If curr node and it's right child has same value
    if (node.right and node.right.val == node.val):
        Rightmax += right + 1
        
    ans[0] = max(ans[0], Leftmax + Rightmax)
    return max(Leftmax, Rightmax)

ans = [0]
length(root1, ans)
print(ans[0])