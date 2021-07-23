class Solution:
    def __init__(self):
        self.res = []

    def subset_sums(self, array, output = []):
        if array == []:
            self.res.append(sum(output))
            return
        
        op2 = output[:]
        output.append(array[0])
        op1 = output[:]
        array = array[1:]
        self.subset_sums(array, op1)
        self.subset_sums(array, op2)
        return

array = [int(i) for i in input().split()]
arr1 =  Solution()
arr1.subset_sums(array)
arr1.res.sort()
print(arr1.res)



