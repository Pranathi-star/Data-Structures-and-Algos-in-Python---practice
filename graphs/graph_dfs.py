def dfs(i, visited, adj_list, seq):
    seq.append(i)
    visited[i] = 1
    for item in adj_list[i]:
        if visited[item] == 0:
            dfs(item, visited, adj_list, seq)  

def dfs_graph(no_nodes, adj_list):
    seq = []
    visited = [0] * (no_nodes + 1)
    for i in range(1, no_nodes + 1):
        if visited[i] == 0:
            dfs(i, visited, adj_list, seq)
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