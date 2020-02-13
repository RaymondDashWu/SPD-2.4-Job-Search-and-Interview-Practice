# Problem 2
# Given an array a of n numbers and a count k find the k largest values in the array a.
# Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  =>  [6, 8, 7]

def k_largest_v1(a, k):
    a.sort()
    # largest_array = []

    # while len(largest_array) != k:
    #     largest_array.append(a.pop())
    # return largest_array
    return a[-k:]

a=[5, 1, 3, 6, 8, 2, 4, 7]
k=3

def k_largest_v2(a, k):
    largest_array = []
    for num in a:
        # initial filling up
        if len(largest_array) != k:
            largest_array.append(num)

        # start to create a stack-like structure that pops smallest and appends new greater #
        temp_min = min(largest_array)
        if num > temp_min:
            largest_array.append(num)
            largest_array.pop(largest_array.index(temp_min))
            # alternative to line above
            # largest_array.remove(temp_min)
    return largest_array

print(k_largest_v1(a, k))
print(k_largest_v2(a, k))