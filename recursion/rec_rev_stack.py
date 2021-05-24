no_el = int(input().strip())
stack = [int(i) for i in input().split()]

def insert_at_begin(temp, stack):
    if len(stack) == 0:
        stack.append(temp)
        return
    last = stack.pop()
    insert_at_begin(temp, stack)
    stack.append(last)
    

def reverse_stack(stack):
    if len(stack) == 1:
        return
    temp = stack.pop()
    reverse_stack(stack)
    insert_at_begin(temp, stack)

reverse_stack(stack)
print(stack)