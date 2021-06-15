def check_cycle(curr_node, parent, visited, adj_list, seq):
    seq.append(curr_node)
    visited[curr_node] = 1
    for item in adj_list[curr_node]:
        if visited[item] == 0:
            if check_cycle(item, curr_node, visited, adj_list, seq):
                return True
        elif item != parent:
            return True
    return False

def dfs_graph(no_nodes, adj_list):
    seq = []
    visited = [0] * (no_nodes + 1)
    for i in range(no_nodes):
        if visited[i] == 0:
            check_cycle(i, -1, visited, adj_list, seq)

    return seq

def main():
    no_nodes, no_edges = [int(i) for i in input().split()]
    adj_list = [0] * (no_nodes + 1)
    for i in range(1, no_nodes + 1):
        adj_list[i] = []
    for i in range(no_edges):
        start, end = [int(i) for i in input().split()]
        adj_list[start].append(end)
        adj_list[end].append(start)
    res = dfs_graph(no_nodes, adj_list)
    print(res)

main()