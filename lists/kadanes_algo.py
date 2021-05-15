def kadanes(no_el, elements):
    current_sum, max_sum = elements[0], elements[0]
    for i in range(1, no_el):
        current_sum += elements[i]
        max_sum = max(current_sum, max_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum


no_el = int(input().strip())
elements = []
for i in range(no_el):
    elements.append(int(input().strip()))
print(kadanes(no_el, elements))
