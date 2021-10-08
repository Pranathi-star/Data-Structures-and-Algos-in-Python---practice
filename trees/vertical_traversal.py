from collections import deque, OrderedDict

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class Solution:
    def __init__(self):
        self.res = []
    def vertical_traversal(self, root):
        if root == None:
            return self.res
        
        queue = deque()
        queue.append(root)

        hdist_from_root = {}
        hdist_from_root[root] = 0

        nodes_dist = {}
        nodes_dist[hdist_from_root[root]] = [root.data]
        while len(queue):
            curr_node = queue.popleft()
            if curr_node.left:
                queue.append(curr_node.left)
                hdist_from_root[curr_node.left] = hdist_from_root[curr_node] - 1
                if nodes_dist.get(hdist_from_root[curr_node.left]) == None:
                    nodes_dist[hdist_from_root[curr_node.left]] = [curr_node.left.data]
                else:
                    nodes_dist[hdist_from_root[curr_node.left]].append(curr_node.left.data)

            if curr_node.right:
                queue.append(curr_node.right)
                hdist_from_root[curr_node.right] = hdist_from_root[curr_node] + 1
                if nodes_dist.get(hdist_from_root[curr_node.right]) == None:
                    nodes_dist[hdist_from_root[curr_node.right]] = [curr_node.right.data]
                else:
                    nodes_dist[hdist_from_root[curr_node.right]].append(curr_node.right.data)

        ans = OrderedDict(sorted(nodes_dist.items()))
        print(ans)
        for i in ans.values():
            for j in i:
                print(j, end = " ")
            print()
            
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.right = TreeNode(5)
root.left.right = TreeNode(2)
tree1 = Solution()
tree1.vertical_traversal(root)
        

