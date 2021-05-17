def fourth_lsb(num):
    binary_str = str(bin(num)[2:])
    length = len(binary_str)
    return binary_str[length - 4]

num = int(input().strip())
print(fourth_lsb(num))