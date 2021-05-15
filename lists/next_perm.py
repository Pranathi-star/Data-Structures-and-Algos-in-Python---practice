def next_perm(num):
    digits = [int(i) for i in str(num)]
    size = len(digits)
    index1 = -1
    for i in range(size - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            index1 = i
            break

    if index1 == -1:
        digits = digits[::-1]
        digits = [str(i) for i in digits]
        return ''.join(digits)
    else:
        for j in range(size - 1, -1, -1):
            if digits[j] > digits[index1]:
                digits[j], digits[index1] = digits[index1], digits[j]
                break
        digits = digits[:index1 + 1] + digits[:index1:-1]
        digits = [str(i) for i in digits]
        return ''.join(digits)

    
    
num = int(input().strip())
print(next_perm(num))