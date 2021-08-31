class Solution:
    def longest_substr_no_repeat(self, string):
        left, right = 0, 0
        curr_str = ""
        size = len(string)
        res = 0
        visited_letters = set()
        while right < size:
            if string[right] in visited_letters:
                while left <= right and string[right] in visited_letters:
                    visited_letters.remove(string[left])
                    left += 1
                    
            curr_str += string[right]
            visited_letters.add(string[right])
            res = max(right - left + 1, res)            
            right += 1
        return res    
            
string = input().strip()
arr1 = Solution()
print(arr1.longest_substr_no_repeat(string))


