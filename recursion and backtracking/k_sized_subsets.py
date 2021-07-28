class Solution:
    def __init__(self):
        self.res = []

    def k_sized_subsets(self, k, array, output = []):
        print(array, output)
        if len(output) == k:
            self.res.append(output)
            return
        if array == []:
            return
        
        op2 = output[:]
        output.append(array[0])
        op1 = output[:]
        array = array[1:]
        self.k_sized_subsets(k, array, op1)
        self.k_sized_subsets(k, array, op2)
        return

array = [i for i in input().split()]
k = int(input().strip())
arr1 =  Solution()
arr1.k_sized_subsets(k, array)
print(arr1.res)



