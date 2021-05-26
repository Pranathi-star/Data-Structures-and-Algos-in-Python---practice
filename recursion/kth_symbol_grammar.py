n = int(input().strip())
k = int(input().strip())

def comp(val):
    if val:
        return 0
    return 1

def kth_in_grammar(n, k):
    if n - 1 == 0 and k - 1 == 0:
        return 0
    else:
        length = pow(2, n - 1)
        mid = length // 2
        if k <= mid:
            return kth_in_grammar(n - 1, k)
        else:
            return comp(kth_in_grammar(n - 1, k - mid))
            
print(kth_in_grammar(n, k))