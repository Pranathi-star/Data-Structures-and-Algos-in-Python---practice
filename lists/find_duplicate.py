#find the duplicate in a list of n + 1 integers ranging from 1 to n
def duplicate(elements):
    slow, fast = elements[0], elements[0]
    slow = elements[slow]
    fast = elements[elements[fast]]
    while(slow != fast):
        slow = elements[slow]
        fast = elements[elements[fast]]

    fast = elements[0]
    while(slow != fast):
        slow = elements[slow]
        fast = elements[fast]

    return slow

no_elements = int(input().strip())
elements = []
for i in range(no_elements):
    elements.append(int(input().strip()))
print(duplicate(elements))



