class Solution:
    def find_celeb(self, mat):
        stack = []
        r = len(stack)
        c = len(stack[0])
        for i in range(r):
            stack.append(i)
        
        while len(stack) >= 2:
            p1 = stack.pop()
            p2 = stack.pop()

            if mat[p1][p2]:
                stack.append(p2)
            else:
                stack.append(p1)
        
        
        celeb = stack.pop()
        
        for i in range(r):
            if mat[celeb][i] or not mat[i][celeb]:
                return -1
                
        return celeb

