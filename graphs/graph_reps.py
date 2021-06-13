no_nodes, no_edges = int(input().strip())

# adjancency matrix method

matrix = [[0] * (no_nodes) + 1] * (no_nodes + 1)

for i in range(no_edges):
    start, end = [int(i) for i in input().split()]
    matrix[start][end] = 1
    matrix[end][start] = 1

# adjancency list method

adj_list = [0] * (no_nodes + 1)
for i in range(1, no_nodes + 1):
    adj_list[i] = []
for i in range(no_edges):
    start, end = [int(i) for i in input().split()]
    adj_list[start].append(end)
    adj_list[end].append(start)

