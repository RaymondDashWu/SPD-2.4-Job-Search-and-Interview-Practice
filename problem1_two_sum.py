# Problem 1
# Given an array a of n numbers and a target value t, find two numbers whose sum is t.
# Example: a=[5, 3, 6, 8, 2, 4, 7], t=10  =>  [3, 7] or [6, 4] or [8, 2]
def two_sum_v1(a, t):
    ref_set = set()
    for num in a:
        if (t - num) in ref_set:
            return [(t - num), num]
        else:
            ref_set.add(num)
    
def two_sum_v2(a, t):
    for num in range(len(a)):
        for other_num in range(1,len(a)):
            if a[num] + a[other_num] == t:
                return [a[num], a[other_num]]
    
def two_sum_v3(a, t):
    a.sort()
    backwards_i = -1
    
    solution_found = False
    while solution_found == False:
        for num in range(len(a)):
            try:
                if a[num] + a[backwards_i] == t:
                    return [a[num], a[backwards_i]]
                else:
                    backwards_i -= 1
            except IndexError:
                continue

a=[5, 3, 6, 8, 2, 4, 7]
t=10
print(two_sum_v1(a, t))
print(two_sum_v2(a, t))
print(two_sum_v3(a, t))