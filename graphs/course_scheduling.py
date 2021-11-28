def topo(i, visited, adj_list, stack):
    visited[i] = 1
    for item in adj_list[i]:
        if visited[item] == 0:
            topo(item, visited, adj_list, stack)
    stack.append(i)  

def topo_sort(no_nodes, adj_list):
    stack = []
    seq = []
    visited = [0] * (no_nodes)
    for i in range(no_nodes):
        if visited[i] == 0:
            topo(i, visited, adj_list, stack)

    for i in range(no_nodes):
        seq.append(stack.pop())
    return seq

def main():
    no_nodes, no_edges = [int(i) for i in input().split()]
    adj_list = [0] * (no_nodes)
    for i in range(no_nodes):
        adj_list[i] = []
    print(adj_list)
    for i in range(no_edges):
        start, end = [int(i) for i in input().split()]
        adj_list[start].append(end)
    res = topo_sort(no_nodes, adj_list)
    print(res)

main()