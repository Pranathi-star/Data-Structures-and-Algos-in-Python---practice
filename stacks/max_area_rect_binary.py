class Solution:
    def get_hist(self, mat, r, c):
        res = []
        for i in range(r):
            if i == 0:
                res.append(mat[0])
            else:
                hist = [0] * c
                for j in range(c):
                    if mat[i][j] == 0:
                        hist[j] = 0
                        continue
                    else:
                        hist[j] = res[-1][j] + mat[i][j]
                res.append(hist)
        return res

    def next_smaller_to_left(self, arr):
        res = []
        stack = []
        size = len(arr)
        for i in range(0, size):
            if len(stack) == 0:
                res.append(-1)
            elif stack[-1][0] < arr[i]:
                res.append(stack[-1][1])
            elif stack[-1][0] >= arr[i]:
                while(len(stack) > 0 and stack[-1][0] >= arr[i]):
                    stack.pop()
                if len(stack) == 0:
                    res.append(-1)
                else:
                    res.append(stack[-1][1])
            stack.append((arr[i], i))
        return res

    def next_smaller_to_right(self, arr):
        res = []
        stack = []
        size = len(arr)
        for i in range(size - 1, -1, -1):
            if len(stack) == 0:
                res.append(size)
            elif stack[-1][0] < arr[i]:
                res.append(stack[-1][1])
            elif stack[-1][0] >= arr[i]:
                while(len(stack) > 0 and stack[-1][0] >= arr[i]):
                    stack.pop()
                if len(stack) == 0:
                    res.append(size)
                else:
                    res.append(stack[-1][1])
            stack.append((arr[i], i))
        return res[::-1]

    def max_area_histogram(self, arr):
        size = len(arr)
        left_small = self.next_smaller_to_left(arr)
        right_small = self.next_smaller_to_right(arr)

        max_area = float('-inf')
        for i in range(0, size):
            left_end = left_small[i]
            right_end = right_small[i]
            max_area = max(max_area, (right_end - left_end - 1)*arr[i])
        return max_area

    def max_rect_bin(self, mat):
        r = len(mat)
        c = len(mat[0])
        hists = self.get_hist(mat, r, c)
        res = float('-inf')
        for i in hists:
            res = max(self.max_area_histogram(i), res)
        return res

matrix = []
r = int(input().strip())
for i in range(r):
    matrix.append([int(i) for i in input().split()])
sol = Solution()
print(sol.max_rect_bin(matrix))
