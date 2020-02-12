# Problem from https://www.geeksforgeeks.org/sort-a-stack-using-recursion/

# NOTES
# Use of any loop constructs like while, for..etc is not allowed

# PSEUDO BRAINSTORM
# main function
# Pop off top element
# peek next element
# recurse function
# call sorting function

# sorting function
# if popped element > peeked element insert peeked
# else keep the same

# python syntax pop, append, [-1]

def sort_stack(arr, num):
    # NOTE: Assuming arr = [-3,18,14,-5] for explanation
    if num > arr[-1]:
        arr.append(num)
    else:
        # Bubble sort-esque way of comparing 2 numbers and then flipping them
        temp = arr.pop()
        arr.append(num)
        arr.append(temp)
        # this method is then recursed
        recursive_stack_sort(arr)
        # On first call it'll give 
        # arr = [-3,14,-5,18]
        # 2nd call
        # arr = [-3,-5,14,18]

def recursive_stack_sort(arr):
    # Base case. An array of length 1 is sorted.
    if len(arr) <= 1:
        return arr
    
    popped = arr.pop()
    recursive_stack_sort(arr)
    sort_stack(arr, popped)




    
# arr = [18, 14, -3, -5]
# arr = [-3,18,14,-5]
arr = [-3,14,18,-5,30]
recursive_stack_sort(arr)
print(arr)