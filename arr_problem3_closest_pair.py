# Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
# Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20  =>  [13, 6] or [4, 17] or [5, 14]

# PSEUDO BRAINSTORM
# convert smaller array into a set

# initiate closest_tracker to keep track of closest overall 
# and temp_closest for each bigger_array element

# initiate element variable that'll keep track of current element
# loop through bigger array and see if t +/- element until an item is found
# if not found, element += 1


# DISCARDED because this would match the first one it finds after initial t - elem ± counter instead
# of closest
# import math

# def closest_pair_v1(a, b, t):
#     closest_tracker = math.inf # keep track of closest overall
#     temp_closest = math.inf # keep track of closest elem

#     # convert smaller array into a set
#     smaller_array = a if len(a) < len(b) else b
#     smaller_set = set()
#     for elem in smaller_array:
#         smaller_set.add(elem)

#     bigger_array = b if len(a) < len(b) else a
#     temp_elem = 0
#     for elem in bigger_array:
#         temp_elem = elem
#         # continually ± 1 until it finds a number AND that number is less than temp_closest until
#         # temp_elem > t
#         while (t - temp_elem) not in smaller_set and (t + temp_elem) not in smaller_set:
#             temp_elem += 1
#         if temp_closest > abs(t - temp_elem - elem):
#             temp_closest = abs(t - temp_elem - elem)
#             closest_tracker = [temp_elem, elem]
#     return closest_tracker

# PSEUDO BRAINSTORM
# sort the arrays
# initialize closest_var

# have 2 pointers: 1 that moves from L => R, 1 that moves R => L
# Idea is that you add small # + big #

# keep track of closest to t and update it if something comes closer

# move pointers when > t

import math
def closest_pair_v2(a, b, t):
    a.sort()
    b.sort()

    smaller_array = a if len(a) < len(b) else b
    bigger_array = a if len(a) > len(b) else b
    l_pointer = 0
    r_pointer = -1

    closest_num = math.inf
    closest_pair = []

    while l_pointer < len(smaller_array) or abs(r_pointer) > len(bigger_array):
        try:
            closest_num = abs(t - (smaller_array[l_pointer] + bigger_array[r_pointer]))
            closest_pair = [smaller_array[l_pointer], bigger_array[r_pointer]]

            # early break condition if the target is found
            if closest_num == 0:
                break

            # test to see if l_pointer + 1 is closer
            if abs(t - (smaller_array[l_pointer + 1] + bigger_array[r_pointer])) <= closest_num: 
                l_pointer += 1    
            else: 
                r_pointer -= 1
        except IndexError:
            break
    return closest_pair

# a=[9, 13, 1, 8, 12, 4, 0, 5]
# b=[19, 17, 40, 140, 62]

a=[9, 13, 1, 8, 12, 4, 0, 5]
b=[3, 17, 4, 14, 6]
t=20
print(closest_pair_v2(a, b, t))