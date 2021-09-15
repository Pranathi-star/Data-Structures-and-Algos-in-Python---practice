class Solution():
    def next_smaller_to_right(self, arr):
        res = []
        stack = []
        size = len(arr)
        for i in range(size - 1, -1, -1):
            if len(stack) == 0:
                res.append(-1)
            elif stack[-1] < arr[i]:
                res.append(stack[-1])
            elif stack[-1] >= arr[i]:
                while(len(stack) > 0 and stack[-1] >= arr[i]):
                    stack.pop()
                if len(stack) == 0:
                    res.append(-1)
                else:
                    res.append(stack[-1])
            stack.append(arr[i])
        return res[::-1]

arr = [int(i) for i in input().split()]
sol = Solution()
print(sol.next_smaller_to_right(arr))
