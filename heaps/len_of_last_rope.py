# the task is to reduce the array to a single element or no element. this is done by taking 2 numbers in the array and replacing them with their absolute difference. find the min length of last rope return 0 if no rope is left.

import heapq
def min_length_rope(no_el, elements):
    size = len(elements)
    for i in range(size):
        elements[i] = (elements[i] * -1)

    heapq.heapify(elements)
    diff = 0
    while(len(elements) > 1):
        op1 = heapq.heappop(elements)
        op2 = heapq.heappop(elements)
        diff = abs(op1 - op2)
        if diff != 0:
            heapq.heappush(elements, -1 * diff)
    
    if len(elements) == 0:
        return 0
    else:
        return -1 * elements[0] 

no_el = int(input().strip())
elements = [int(i) for i in input().split()]
print(min_length_rope(no_el, elements))