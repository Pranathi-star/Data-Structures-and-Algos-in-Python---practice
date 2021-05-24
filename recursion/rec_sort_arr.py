def rec_insert(elements, term):
    if len(elements) == 0 or elements[len(elements) - 1] <= term:
        elements.append(term)
        return
    
    temp = elements[len(elements) - 1]
    elements.pop()
    rec_insert(elements, term)
    elements.append(temp)

def rec_sort(elements):
    if len(elements) == 1:
        return
    temp = elements[len(elements) - 1]
    elements.pop()
    rec_sort(elements)
    rec_insert(elements, temp)
    return elements

elements = [int(i) for i in input().split()]
print(rec_sort(elements))


