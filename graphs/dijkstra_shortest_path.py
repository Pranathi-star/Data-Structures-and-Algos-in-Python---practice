from heapq import heappush, heappop, heapify
from sys import maxsize

def dijkstra(no_nodes, distance_to, adj_list, source):
    priority_queue = []
    heapify(priority_queue)
    distance_to[source] = 0
    heappush(priority_queue, (distance_to[source], source))
    while(len(priority_queue) > 0):
        curr_dist, curr_node = heappop(priority_queue)
        for item in adj_list[curr_node]:
            next_node = item[0]
            next_dist = item[1]
            if distance_to[next_node] > (distance_to[curr_node] + next_dist):
                distance_to[next_node] = (distance_to[curr_node] + next_dist)
                heappush(priority_queue, (distance_to[next_node], next_node))
    
    return distance_to[1:]

def main():
    no_nodes, no_edges = [int(i) for i in input().split()]
    distance_to = [maxsize] * (no_nodes + 1)
    adj_list = [0] * (no_nodes + 1)
    for i in range(1, no_nodes + 1):
        adj_list[i] = []

    for i in range(no_edges):
        start, end, wt = [int(i) for i in input().split()]
        adj_list[start].append((end, wt))
        adj_list[end].append((start, wt))
    print(adj_list)
    source = int(input().strip())
    print(dijkstra(no_nodes, distance_to, adj_list, source))

main()