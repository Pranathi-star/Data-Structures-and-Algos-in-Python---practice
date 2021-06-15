from collections import deque 

def check_cycle(no_nodes, adj_list, visited):
    for i in range(1, no_nodes + 1):
        if visited[i] == 0:
            queue = deque()
            queue.append([i, -1])
            visited[i] = 1
            while(len(queue) > 0):
                curr_node = queue.popleft()
                val = curr_node[0]
                prev = curr_node[1]
                for item in adj_list[val]:
                    if visited[item] == 0:
                        queue.append([item, val])
                        visited[item] = 1

                    elif prev != item:
                        return True

    return False

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
    print(check_cycle(no_nodes, adj_list, visited))

main()