from collections import deque

def check_bipartite(no_nodes, src, colour_assign, adj_list):
    queue = deque()
    queue.append(src)
    colour_assign[src] = 1
    while(len(queue) > 0):
        curr_node = queue.popleft()
        for item in adj_list[curr_node]:
            if colour_assign[item] == -1:
                colour_assign[item] = 1 - colour_assign[curr_node]
                queue.append(item)
            elif colour_assign[item] == colour_assign[curr_node]:
                return False
    return True
    
def main():
    no_nodes, no_edges = [int(i) for i in input().split()]
    colour_assign = [-1] * (no_nodes + 1)
    adj_list = [0] * (no_nodes + 1)
    for i in range(1, no_nodes + 1):
        adj_list[i] = []

    for i in range(no_edges):
        start, end = [int(i) for i in input().split()]
        adj_list[start].append(end)
        adj_list[end].append(start)
    
    flag = 0
    for i in range(1, no_nodes + 1):
        if colour_assign[i] == -1:
            if check_bipartite(no_nodes, i, colour_assign, adj_list) == False:
                print(False)
                flag = 1
                break
    if flag == 0: print(True)

main()