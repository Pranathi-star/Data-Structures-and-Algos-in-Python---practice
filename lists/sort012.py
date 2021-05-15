# sort an array containing only 0's, 1's and 2's with extra space
def counting_sort(no_el, elements):
    count = [0] * 3
    pos = [0] * 3
    sorted_arr = [0] * no_el 
    for i in range(no_el):
        count[elements[i]] += 1
    
    for j in range(1, 3):
        pos[j] = pos[j - 1] + count[j - 1]

    for k in range(no_el):
        sorted_arr[pos[elements[k]]] = elements[k]
        pos[elements[k]] += 1
    return sorted_arr

no_el = int(input().strip())
elements = []
for i in range(no_el):
    elements.append(int(input().strip()))
print(counting_sort(no_el, elements))

