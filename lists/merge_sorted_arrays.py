def insertion_sort(no_el, arr):
    for i in range(no_el):
        key = arr[i]
        j = i - 1
        while(j >= 0 and key < arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
     
def merge(no_big, big_arr, no_small, small_arr):
    for i in range(no_big):
        if big_arr[i] <= small_arr[0]:
            continue
        else:
            big_arr[i], small_arr[0] = small_arr[0], big_arr[i]
            small_arr = insertion_sort(no_small, small_arr)
    return big_arr, small_arr

n1 = int(input().strip())
arr1 = []
for i in range(n1):
    arr1.append(int(input().strip()))

arr2 = []
n2 = int(input().strip())
for i in range(n2):
    arr2.append(int(input().strip()))

if n1 >= n2:
    print(merge(n1, arr1, n2, arr2))
else:
    print(merge(n2, arr2, n1, arr1))

