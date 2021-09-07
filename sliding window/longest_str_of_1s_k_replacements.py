class Solution:
    def longest_substr_1s(self, string, k):
        left, right, count_1s = 0, 0, 0
        size = len(string)
        res = 0

        while right < size:
            if string[right] == "1":
                count_1s += 1
            
            if(right - left + 1 - count_1s) > k:
                if string[left] == "1":
                    count_1s -= 1
                left += 1       

            res = max(right - left + 1, res)
            right += 1
        return res    
            
string = input().strip()
k = int(input().strip())
str1 = Solution()
print(str1.longest_substr_1s(string, k))


