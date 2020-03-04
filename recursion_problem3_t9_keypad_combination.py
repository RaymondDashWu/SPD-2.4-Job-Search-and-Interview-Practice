# Given a string of digits 2 to 9 a user has pressed on a T9 “old school” telephone keypad, return a list of all letter combinations they could have been trying to type on the keypad.
# Example execution 1:  t9_letters("23")  ⇒  ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
# Example execution 2:  t9_letters("4663")  ⇒  ["gmmd", …, "gone", …, "good", …, "home", …, "hood", …, "ioof"]

# Keypad image used for reference
# https://www.researchgate.net/profile/Thad_Starner/publication/221270510/figure/fig1/AS:305581094129666@1449867618762/The-12-key-keypad-for-a-Motorola-Razr.png

# Assumptions
# dictionary of mappings given

# PSEUDO BRAINSTORM
# base case when there is no next digit in first number of string. SCRATCHED for len of array

# initialize variable on empty string. To be used to combine letters later
# keep track of 2 indexes
# first one will be per number
# 2nd one will be letter per letter at number
# recursively call after number is iterated through at letter + 1
# append combined letter string to output? Unsure of order

# NOTE TODO Unfinished

t9_keypad_mappings = {
    2: ("a", "b", "c"),
    3: ("d", "e", "f"),
    4: ("g", "h", "i"),
    5: ("j", "k", "l"),
    6: ("m", "n", "o"),
    7: ("p", "q", "r", "s"),
    8: ("t", "u", "v"),
    9: ("w", "x", "y", "z"),
}

def valid_t9_conversion_and_length(str_numbers):
    """Used to check if the numbers being input are valid for a t9 conversion. 
    Ex: 0, 1, symbols, letters are not allowed
    
    Added length calculation since we're looping through anyways. To be used in t9_letters function as
    part of the base case. Will calculate the total length the output should be"""
    valid_numbers = ["2","3","4","5","6","7","8","9"]
    total_len = 0
    for num in str_numbers:
        if num in valid_numbers:
            total_len += len(t9_keypad_mappings[int(num)])
        else:
            return ValueError
    return total_len


def t9_letters(str_numbers, valid = False, lett_ind = 0, len_total = 0, output_arr = []):
    if valid == False: # First check
        # From earlier valid_t9_conversion_and_length fn.
        # Calculates how long the array should be.
        # Ex: if string is "23" len of 2 & 3 at t9_keypad_mappings is 3 * 3 = 9. Total array length should be 9
        len_total = valid_t9_conversion_and_length(str_numbers) 
        valid = True
    # Base case
    if len(output_arr) == len_total: 
        return output_arr

    # [2,3]
    split_str = [int(num) for num in str_numbers]

# initialize variable on empty string. To be used to combine letters later
# keep track of 2 indexes
# first one will be per number
# 2nd one will be letter per letter at number
# recursively call after number is iterated through at letter + 1
# append combined letter string to output? Unsure of order
# print(t9_keypad_mappings[[2][0]][0])

    for num_ind in range(len(split_str)):
        append_to_arr = ""
        print(t9_keypad_mappings[split_str[num_ind]][lett_ind])
        append_to_arr += t9_keypad_mappings[split_str[num_ind]][lett_ind]
        t9_letters(str_numbers, valid = valid, lett_ind = lett_ind + 1, len_total = len_total, output_arr = output_arr)
        output_arr.append(append_to_arr)
    # pass

if __name__ == "__main__":
    print(t9_letters("23"))
    assert t9_letters("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    # print(t9_letters("4663"))