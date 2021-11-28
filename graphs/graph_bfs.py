from collections import deque

def bfs(no_nodes, visited, adj_list):
    seq = []
    for i in range(1, no_nodes + 1):
        if(visited[i] == 0):
            queue = deque()
            queue.append(i)
            visited[i] = 1
            while(len(queue) > 0):
                curr_level = []
                for i in range(len(queue)):
                    curr_node = queue.popleft()
                    curr_level.append(curr_node)
                    for item in adj_list[curr_node]:
                        if(visited[item] == 0):
                            queue.append(item)
                            visited[item] = 1
                seq.append(curr_level)
    return seq

def main():
    no_nodes, no_edges = [int(i) for i in input().split()]
    visited = [0] * (no_nodes + 1)
    adj_list = [0] * (no_nodes + 1)
    for i in range(1, no_nodes + 1):
        adj_list[i] = []

    for i in range(no_edges):
        start, end = [int(i) for i in input().split()]
        adj_list[start].append(end)
        adj_list[end].append(start)
    print(bfs(no_nodes, visited, adj_list))

main()