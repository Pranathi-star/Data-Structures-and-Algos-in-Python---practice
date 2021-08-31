class Solution:
    def longest_substr_k_unique(self, string, k):
        left, right = 0, 0
        curr_str = ""
        size = len(string)
        res = 0
        visited_letters = {}
        while right < size:
            curr_str += string[right]
            if string[right] in visited_letters:
                visited_letters[string[right]] += 1
            else:
                visited_letters[string[right]] = 1

            while len(visited_letters) > k:
                if string[left] in visited_letters:
                    visited_letters[string[left]] -= 1
                    if visited_letters[string[left]] == 0:
                        del visited_letters[string[left]]
                        
                curr_str = curr_str[1:]
                left += 1

            if len(visited_letters) == k:
                res = max(right - left + 1, res)            
            right += 1
        return res    
            
string = input().strip()
k = int(input().strip())
arr1 = Solution()
print(arr1.longest_substr_k_unique(string, k))


