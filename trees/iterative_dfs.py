from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class Solution:
    def __init__(self):
        self.res = []
    def preorder_iter(self, root):
        if root == None:
            return self.res
        
        stack = []
        stack.append(root)
        while len(stack):
            curr_node = stack.pop()
            self.res.append(curr_node.data)
            if curr_node.right:
                stack.append(curr_node.right)
            if curr_node.left:
                stack.append(curr_node.left)

        return self.res

    def inorder_iter(self, root):
        self.res = []
        curr_node = root
        if curr_node == None:
            return self.res
        stack = []
        while True:
            if curr_node != None:
                stack.append(curr_node)
                curr_node = curr_node.left
            else:
                if len(stack) == 0:
                    break
                curr_node = stack.pop()
                self.res.append(curr_node.data)
                curr_node = curr_node.right
        return self.res
            
    def postorder_iter(self, root):
        stack1, stack2 = [], []
        self.res = []
        if root == None:
            return self.res
        stack1.append(root)
        while stack1:
            curr_node = stack1.pop()
            stack2.append(curr_node)
            if curr_node.left:
                stack1.append(curr_node.left)
            if curr_node.right:
                stack1.append(curr_node.right)
            
        while stack2:
            self.res.append(stack2.pop().data)
        
        return self.res   

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.right = TreeNode(5)
root.left.right = TreeNode(2)

tree1 = Solution()
print(tree1.preorder_iter(root))
print(tree1.inorder_iter(root))        
print(tree1.postorder_iter(root))
