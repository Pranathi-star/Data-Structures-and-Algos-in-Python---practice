class Solution:
    def longest_substr_same_letter(self, string, k):
        left, right, max_freq = 0, 0, 0
        size = len(string)
        res = 0
        freq = {}

        while right < size:
            if string[right] in freq:
                freq[string[right]] += 1
            else:
                freq[string[right]] = 1
            
            max_freq = max(freq.values())

            while right - left + 1 - max_freq > k:
                freq[string[left]] -= 1
                left += 1 

            res = max(right - left + 1, res)
            right += 1
        return res    
            
string = input().strip()
k = int(input().strip())
str1 = Solution()
print(str1.longest_substr_same_letter(string, k))


