# Question 1: Given a string containing just the characters (, ), {, }, [ and ], determine if the input string is valid. Criteria:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Examples: 
# "" --> valid
# "{[()]}" --> valid
# "{]{" --> invalid
# Stretch challenge: 
# (1) Handle strings with other characters 
# (2) Expand to handle any <tag> and ensure it is closed with corresponding </tag>

# PSEUDO BRAINSTORM
# initialize a stack that will be used for testing opposite bracket
# ignore anything that's not a bracket
# for each bracket append the opposite to the stack
# see if the latest element (should be opposite bracket) in stack is equal to the next character.
# If it is then pop it off. Next character must be the next element
# keep doing this until len(stack) == 0 or a character doesn't match

# Assumptions
# there is a pre-made dict that contains the associated brackets

# NOTE TODO Unfinished

bracket_dict = {
    "{":"}",
    "(":")",
    "[":"]",
    "<":">"
}

def test_valid(string):
    if len(string) == 0:
        return True

    bracket_stack = []

    for char in string:
        if char not in (bracket_dict.keys()|bracket_dict.values()): # if there's a character that's not a bracket
            continue
        if char in bracket_dict.keys():
            bracket_stack.append(bracket_dict[char]) # Should append opposite bracket
        elif char == bracket_stack[-1]: # last bracket in stack should be char to pop
            bracket_stack.pop()
    if len(bracket_stack) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    string = ""
    assert test_valid(string) == True
    string = "{[()]}"
    assert test_valid(string) == True
    string = "{]{"
    assert test_valid(string) == False
    string = "{[asd()]gs}"
    assert test_valid(string) == True
    string = "<tag></tag>"
    assert test_valid(string) == True
    string = "<tag><tag>"
    assert test_valid(string) == False