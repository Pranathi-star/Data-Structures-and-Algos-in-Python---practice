class Solution:
    def __init__(self):
        self.res = []

    def find_perms(self, output, freq, array):
        if len(output) == len(array):
            self.res.append(output)
        for i in range(len(array)):
            if freq[i] == 0:
                output.append(array[i])
                freq[i] = 1
                self.find_perms(output[:], freq[:], array)
                freq[i] = 0
                output.pop()

array = [int(i) for i in input().split()]
arr1 = Solution()
output = []
freq = [0 for i in range(len(array))]
arr1.find_perms(output, freq, array)
print(arr1.res)