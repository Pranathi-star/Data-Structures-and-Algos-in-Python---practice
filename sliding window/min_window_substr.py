class Solution:
    def smallest_window_substr(self, string, portion_str):
        freq ={}
        for i in portion_str:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        size = len(string)
        count_non_zero = len(freq)
        left, right = 0, 0
        res = float('inf')

        while right < size:
            if string[right] in freq:
                freq[string[right]] -= 1
                if freq[string[right]] == 0:
                    count_non_zero -= 1

            if count_non_zero > 0:
                right += 1

            elif count_non_zero == 0:
                while count_non_zero == 0:
                    res = min(res, right - left + 1)
                    if string[left] in freq:
                        freq[string[left]] += 1
                        if freq[string[left]] == 1:
                            count_non_zero += 1
                    left += 1    
                right += 1

        return res

string = input().strip()
portion_str = input().strip()
str1 = Solution()
print(str1.smallest_window_substr(string, portion_str))

