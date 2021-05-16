def left_rotate(no_el, no_rotations, elements):
    return elements[no_rotations%no_el:] + elements[:no_rotations%no_el]

no_el = int(input().strip())
elements = [int(i) for i in input().split()]
no_rotations = int(input().strip())
print(left_rotate(no_el, no_rotations, elements))

