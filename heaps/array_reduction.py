# the task is to reduce the array to a single element. this is done by adding 2 numbers in the array and replacing them with their sum. the cost of such an operation is the sum itself. do this process with minimum cost
import heapq
def min_cost_reduction(no_el, elements):
    heapq.heapify(elements)
    min_cost = 0
    while(len(elements) > 1):
        op1 = heapq.heappop(elements)
        op2 = heapq.heappop(elements)
        min_cost += (op1 + op2)
        heapq.heappush(elements, op1 + op2)
    return min_cost    

no_el = int(input().strip())
elements = [int(i) for i in input().split()]
print(min_cost_reduction(no_el, elements))