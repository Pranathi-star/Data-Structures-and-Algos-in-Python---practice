class Solution:
    def __init__(self):
        self.anagrams = set()

    def gen_perms(self, array, l, r):
        if l == r:
            self.anagrams.add(''.join(array))
        else:
            for i in range(l, r + 1):
                array[l], array[i] = array[i], array[l]
                self.gen_perms(array, l + 1, r)
                array[l], array[i] = array[i], array[l]

    def count_anagrams(self, string, portion_str):
        self.gen_perms(list(portion_str), 0, len(portion_str) - 1)
        print(self.anagrams)
        size = len(string)
        k = len(portion_str)
        left, right = 0, 0
        res = 0
        curr_str = ""
        while right < size:
            curr_str += string[right]
            if right - left + 1 < k:
                right += 1
            elif right - left + 1 == k:
                if curr_str in self.anagrams:
                    res += 1
                curr_str = curr_str[1:]
                left += 1
                right += 1
        return res

string = input().strip()
portion_str = input().strip()
str1 = Solution()
print(str1.count_anagrams(string, portion_str))

