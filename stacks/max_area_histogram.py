class Solution:
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
        print(left_small, right_small)

        max_area = float('-inf')
        for i in range(0, size):
            print(i)
            left_end = left_small[i]
            right_end = right_small[i]
            max_area = max(max_area, (right_end - left_end - 1)*arr[i])
        return max_area

arr= [int(i) for i in input().split()]
sol = Solution()
print(sol.max_area_histogram(arr))

