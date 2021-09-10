# given a string of only stars and bars, find the number of stars between bars

def closest_bar_index(s, start, end):
    start_end = [-1, -1]
    for i in range(start, end + 1):
        if s[i] == "|":
            start_end[0] = i
            break
    for i in range(end, start - 1, -1):
        if s[i] == "|":
            start_end[1] = i
            break
    return start_end
    
def stars_bars(s, length, no_indices, start_indices, end_indices):
    res = []
    stars_upto = [0]*length
    if s[0] == "*":
        stars_upto[0] == 1
    for i in range(1, length):
        if s[i] == "|":
            stars_upto[i] = stars_upto[i - 1]
        else:
            stars_upto[i] = stars_upto[i - 1] + 1
    print(stars_upto)
    for i in range(no_indices):
        start = start_indices[i] - 1
        end = end_indices[i] - 1
        start_end_bars = closest_bar_index(s, start, end)
        res.append(stars_upto[start_end_bars[1]] - stars_upto[start_end_bars[0]])
    return res
    
s = input().strip()
length = len(s)
no_indices = int(input().strip())
start_indices = [int(i) for i in input().split()]
end_indices = [int(i) for i in input().split()]
print(stars_bars(s, length, no_indices, start_indices, end_indices))
