from functools import cmp_to_key

@cmp_to_key
def custom_cmp(a, b):
    if str(a) + str(b) < str(b) + str(a):
        return 1
    elif str(a) + str(b) > str(b) + str(a):
        return -1
    else:
        return 0

def max_num_poss(nums):
    nums.sort(key = custom_cmp)
    return ''.join(map(str, nums))
            
nums = [i for i in input().split()]
print(max_num_poss(nums))
    
