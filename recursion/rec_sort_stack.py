no_el = int(input().strip())
stack = [int(i) for i in input().split()]

def insert_in_stack(stack, top_el):
    if len(stack) == 0:
        stack.append(top_el)
    elif(stack[-1] <= top_el):
        stack.append(top_el)
    else:
        temp = stack.pop()
        insert_in_stack(stack, top_el)
        stack.append(temp)


def sort_stack(stack):
    if len(stack) == 1:
        return
    top_el = stack.pop()
    sort_stack(stack)
    insert_in_stack(stack, top_el)

sort_stack(stack)
print(stack)