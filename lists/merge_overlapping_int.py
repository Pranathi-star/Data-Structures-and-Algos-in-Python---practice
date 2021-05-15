# merge overlapping intervals
def merge_intervals(no_el, elements):
    elements.sort()
    res = []
    pair = elements[0]
    for i in elements:
        if i[0] < pair[1]:
            pair[1] = max(pair[1], i[1])
        else:
            res.append(pair)
            pair = i
    res.append(pair)
    return res

no_el = int(input().strip())
elements = []
for i in range(no_el):
    elements.append([int(i) for i in input().split()])
print(merge_intervals(no_el, elements))
