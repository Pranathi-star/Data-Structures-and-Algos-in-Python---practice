class Solution:
    def __init__(self, array):
        self.array = array

    def insert_in_arr(self, last_element):
        if len(self.array) == 0:
            self.array.append(last_element)
            return
        elif last_element >= self.array[-1]:
            array.append(last_element)
            return
        temp = array.pop()
        self.insert_in_arr(last_element)
        self.array.append(temp)
        return

    def sort_array(self):
        if len(self.array) == 1 or len(self.array) == 0:
            return self.array
        last_element = self.array.pop()
        self.array = self.sort_array()
        self.insert_in_arr(last_element)
        return self.array

array = [int(i) for i in input().split()]
arr1 = Solution(array)
print(arr1.sort_array())