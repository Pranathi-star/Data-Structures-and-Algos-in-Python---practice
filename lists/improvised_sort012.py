def dutch_national(no_el, elements):
    low, mid, high = 0, 0, no_el - 1
    while mid <= high:
        if elements[mid] == 0:
            elements[mid], elements[low] = elements[low], elements[mid]
            low += 1
            mid += 1
            
        elif elements[mid] == 1:
            mid += 1
            
        elif elements[mid] == 2:
            elements[high], elements[mid] = elements[mid], elements[high]
            high -= 1
    return elements

no_el = int(input().strip())
elements = []
for i in range(no_el):
    elements.append(int(input().strip()))
print(dutch_national(no_el, elements))