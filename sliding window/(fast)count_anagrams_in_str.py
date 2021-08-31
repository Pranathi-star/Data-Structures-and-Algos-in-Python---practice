class Solution:
    def count_anagrams(self, string, portion_str):
        freq ={}
        for i in portion_str:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        size = len(string)
        k = len(portion_str)
        left, right = 0, 0
        res = 0
        curr_str = ""
        temp = freq.copy()
        while right < size:
            curr_str += string[right]
            if string[right] in temp:
                temp[string[right]] -= 1

            if right - left + 1 < k:
                right += 1
            elif right - left + 1 == k:
                if not any(temp.values()):
                    res += 1
                if curr_str[0] in freq:  
                    temp[curr_str[0]] += 1
                curr_str = curr_str[1:]
                left += 1
                right += 1

        return res

string = input().strip()
portion_str = input().strip()
str1 = Solution()
print(str1.count_anagrams(string, portion_str))

