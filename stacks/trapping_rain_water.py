class Solution:
    def find_max_left(self, arr, size):
        mxl = [0] * size
        mxl[0] = arr[0]
        for i in range(1, size):
            mxl[i] = max(mxl[i - 1], arr[i])
        return mxl

    def find_max_right(self, arr, size):
        mxr = [0] * size
        mxr[size - 1] = arr[size - 1]
        for i in range(size - 2, -1, -1):
            mxr[i] = max(mxr[i + 1], arr[i])
        return mxr

    def trapping_rain_water(self, arr):
        size = len(arr)
        water_on_bar = []
        mxl = self.find_max_left(arr, size)
        mxr = self.find_max_right(arr, size)
        for i in range(size):
            max_ht_water = min(mxl[i], mxr[i])
            water_on_bar.append(max_ht_water - arr[i])
        return sum(water_on_bar) 

arr = [int(i) for i in input().split()]
sol = Solution()
print(sol.trapping_rain_water(arr))