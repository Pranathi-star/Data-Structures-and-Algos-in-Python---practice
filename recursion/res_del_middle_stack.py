def del_mid(stack, mid_index):
    if mid_index == 0:
        stack.pop()
        return
    temp = stack.pop()
    del_mid(stack, mid_index - 1)
    stack.append(temp)

no_el = int(input().strip())
stack = [int(i) for i in input().split()]
mid_index = no_el // 2
del_mid(stack, mid_index)
print(stack)