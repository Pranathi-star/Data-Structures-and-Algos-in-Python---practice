from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class Solution:
    def __init__(self):
        self.res = []

    def zigzag_traversal(self, root, flag):
        if root == None:
            return self.res
        
        queue = deque()
        queue.append(root)
        while len(queue) != 0:
            curr_level = []
            flag = abs(1 - flag)
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                curr_level.append(curr_node.data)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            if flag:
                self.res.append(curr_level)
            else:
                self.res.append(curr_level[::-1])
        return self.res
            
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.right = TreeNode(5)
root.left.right = TreeNode(2)
tree1 = Solution()
print(tree1.zigzag_traversal(root, flag = 0))
        

