class Solution:
    def no_terms_lt_on_left(self, arr):
        stack = []
        res = []
        size = len(arr)
        for i in range(size):
            if len(stack) == 0:
                res.append(1)

            elif arr[i] <= arr[stack[-1]]:
                res.append(i - stack[-1])
            
            elif arr[i] > arr[stack[-1]]:
                while len(stack) > 0 and arr[i] > arr[stack[-1]]:
                    stack.pop()

                if len(stack) == 0:
                    res.append(1)
                else:
                    res.append(i - stack[-1])
            
            stack.append(i)
        return res

arr = [int(i) for i in input().split()]
sol = Solution()
print(sol.no_terms_lt_on_left(arr))




