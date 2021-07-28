class Solution:
    def string_is_palidrome(self, start, end, string):
        while start <= end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        return True

    def palindromic_partitioning(self, idx, string, output, res):
        if idx == len(string):
            res.append(output)
            return
        for i in range(idx, len(string)):
            if self.string_is_palidrome(idx, i, string[:]):
                print(string[idx: i + 1])
                output.append(string[idx: idx + (i - idx + 1)])
                self.palindromic_partitioning(i + 1, string, output[:], res)
                output.pop()

string = input().strip()
str1 = Solution()
res = []
output = []
str1.palindromic_partitioning(0, string, output, res)
print(res)


