num = int(input().strip())
positions = [int(i + 1) for i in range(num)]
k = int(input().strip())
curr_index = 0

def josepheus(positions, curr_index, k):
    if len(positions) == 1:
        return positions[0]
    new_start = (curr_index + k - 1) % len(positions)
    positions.pop(new_start)
    return josepheus(positions, new_start, k)

print(josepheus(positions, curr_index, k))
