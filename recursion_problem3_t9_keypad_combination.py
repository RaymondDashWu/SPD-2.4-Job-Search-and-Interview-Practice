# Given a string of digits 2 to 9 a user has pressed on a T9 “old school” telephone keypad, return a list of all letter combinations they could have been trying to type on the keypad.
# Example execution 1:  t9_letters("23")  ⇒  ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
# Example execution 2:  t9_letters("4663")  ⇒  ["gmmd", …, "gone", …, "good", …, "home", …, "hood", …, "ioof"]

# Keypad image used for reference
# https://www.researchgate.net/profile/Thad_Starner/publication/221270510/figure/fig1/AS:305581094129666@1449867618762/The-12-key-keypad-for-a-Motorola-Razr.png

# Assumptions
# dictionary of mappings given

# PSEUDO BRAINSTORM

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

def valid_t9_conversion(str_numbers):
    """Used to check if the numbers being input are valid for a t9 conversion. 
    Ex: 0, 1, symbols, letters are not allowed"""
    valid_numbers = ["2","3","4","5","6","7","8","9"]

    for num in str_numbers:
        if num in valid_numbers:
            continue
        else:
            return ValueError

def t9_letters(str_numbers, valid = False):
    if valid == False:
        valid_t9_conversion(str_numbers)
        valid = True
    # pass

if __name__ == "__main__":
    assert t9_letters("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    print(t9_letters("4663"))