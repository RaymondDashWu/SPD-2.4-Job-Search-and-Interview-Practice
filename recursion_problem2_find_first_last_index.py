# Given a sorted array of strings, write a recursive function to find the index of the first and last occurrence of a target string. If the target string is not found in the array, report that.
# Example input:  instructors = [Adriana, Adriana, Alan, Alan, Alan, Alan, Alan, Braus, Braus, Braus, Braus, Dan, Dan, Dan, Dan, Dan, Dani, Dani, Jess, Meredith, Milad, Milad, Mitchell, Mitchell, Mitchell, Mitchell]
# Example execution:  find_indexes(instructors, 'Braus')  ⇒  (7, 10)

# PSEUDO BRAINSTORM 1 - Scratched. O(n) but there's a more efficient way since it comes pre-sorted
# initialize a ind_tracker that will be used to keep track of indexes
# initialize index array based on ind_tracker
# base case when there is something in ind_arr and next instructor is not target
# when the target instructor is found append ind_tracker to ind_arr

# PSEUDO BRAINSTORM 2 - Binary search
# initiate a middle argument that will be used to find midpoint
# base case when there is something in ind_arr and next instructor is not target
# change middle based on whether the name is greater or less than target
# append the middle to ind_arr when its equal to target
# after target is found, check to see if name to left is target
# keep going until no longer equal to target

# TODO temporarily made right 26. Figure out how to do later
def find_indexes(arr_instructors, target, left, right, middle, ind_arr = []):
    if len(ind_arr) == 2:
        return ind_arr

    # For finding target via binary search initially
    while arr_instructors[middle] != target:
        middle = (left + right) // 2
        if arr_instructors[middle] == target:
            break
        if arr_instructors[middle] > target:
            return find_indexes(arr_instructors, target, left = 0, right = middle, middle = middle)
        else:
            return find_indexes(arr_instructors, target, left = middle, right = right, middle = middle)
    
    # if arr_instructors[middle] == target:
    #     return True

    # after target is found, check to see if name to left is target
    # keep going until no longer equal to target
    while arr_instructors[middle] == target:
        if arr_instructors[middle - 1] == target and len(ind_arr) == 0:
            return find_indexes(arr_instructors, target, left, right = right - 1, middle = middle - 1)
        if arr_instructors[middle + 1] != target and len(ind_arr) == 1:
            ind_arr.append(middle) # append upper bound but only after lower bound has been found
            return ind_arr
        else:
            if len(ind_arr) == 0:
                ind_arr.append(middle) # appending lower bound
                # break
            else:
                return find_indexes(arr_instructors, target, left, right, middle = middle + 1)

    # while (arr_instructors[middle-1], arr_instructors[middle], arr_instructors[middle+1]) != target:
    #     return find_indexes(arr_instructors, target, middle = 1, ind_arr = [])

if __name__ == "__main__":
    instructors = ["Adriana", "Adriana", "Alan", "Alan", "Alan", "Alan", "Alan", "Braus", "Braus", "Braus", "Braus", "Dan", "Dan", "Dan", "Dan", "Dan", "Dani", "Dani", "Jess", "Meredith", "Milad", "Milad", "Mitchell", "Mitchell", "Mitchell", "Mitchell"]
    print("Should be (7, 10)", find_indexes(instructors, 'Braus', left = 0, right = len(instructors), middle = (0+len(instructors))//2))