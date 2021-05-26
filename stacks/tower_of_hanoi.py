no_el = int(input().strip())
stack1 = [int(i) for i in input().split()]
stack2 = [] * no_el
stack3 = [] * no_el

def tower_of_hanoi(no_el, stack1, stack2, stack3):
    if no_el == 0:
        return
    tower_of_hanoi(no_el - 1, stack1, stack3, stack2)
    stack3.append(stack1.pop())
    tower_of_hanoi(no_el - 1, stack2, stack1, stack3)

tower_of_hanoi(no_el, stack1, stack2, stack3)
print(stack1)
print(stack2)
print(stack3)