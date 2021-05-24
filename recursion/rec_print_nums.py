def print_nums_upto(num):
    if num == 1:
        print(num, end = " ")
        return
    print_nums_upto(num - 1)
    print(num, end = " ")

num = int(input().strip())
print_nums_upto(num)