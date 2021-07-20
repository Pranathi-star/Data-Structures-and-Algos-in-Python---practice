class Solution:
    def __init__(self):
        self.res = set()

    def perms_of_list(self, array, l, r):
        if l == r:
            self.res.add(''.join(array))
        else:
            for i in range(l, r + 1):
                array[l], array[i] = array[i], array[l]
                self.perms_of_list(array, l + 1, r)
                array[l], array[i] = array[i], array[l]
        

array = [i for i in input().split()]
array1 = Solution()
array1.perms_of_list(array, 0, len(array) - 1)
print(list(array1.res))