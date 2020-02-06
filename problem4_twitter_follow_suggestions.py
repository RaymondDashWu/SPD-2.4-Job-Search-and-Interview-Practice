# You’re working an internship at Twitter and are tasked to improve suggestions 
# for accounts to follow, which already works great for established accounts 
# because it uses content from your tweets and other accounts you follow to suggest 
# new ones. However, when a new user signs up none of this information exists yet, 
# but Twitter still wants to make some follow suggestions. Your team asked you to 
# implement a function that accepts a new user’s handle and an array of many other 
# users’ handles, which could be very long – Twitter has over 330 million active 
# accounts! You need to calculate a similarity score between a pair of handles by 
# looking at the letters each contains, scoring +1 for each letter in the alphabet 
# that occurs in both handles but scoring –1 for each letter that occurs in only one 
# handle. Your function should return k handles from the array that have the highest 
# similarity score to the new user’s handle.

# Example execution:
# handles = ['DogeCoin', 'YangGang2020', 'HodlForLife', 'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust']
# suggest('iLoveDogs', handles, k=2)   should return   ['GodIsLove', 'DogeCoin']

# PSEUDO BRAINSTORM
# I assume lowercase because I don't think capitals make a difference in following someone
# assumed that multiple letters of the same increased point value. Ex: if name is "DDDDD", handle "DogD" score would be 5 * 2 = 10

# lowercase and split letters of name
# put letters into a name_point_dict of {{letter1: # occurences}, {letter2: # occurences}, ...}

# split letter in each handle
# if that letter is in name, + value at that letter

# create new dictionary with {{handle: score}, ...}
# return 2 highest scores
from heapq import nlargest 

def suggest(name, handles, k):
    name_dict = {}
    # lowercase and split letters of name
    split_name = [char for char in name.lower()]
    # will put letters into a name_dict {{letter1: # occurences}, {letter2: # occurences}, ...}
    for letter in split_name:
        if letter not in name_dict:
            name_dict[letter] = 1
        else:
            name_dict[letter] += 1

    # Will store {{handle: score}, ...} and return top k values
    result_dict = {}

    for name in handles:
        split_handle = [char for char in name.lower()]
        temp_score = 0
        
        for char in split_handle:
            if char in name_dict:
                temp_score += name_dict[char]
            else:
                temp_score -= 1
        result_dict[name] = temp_score
    # TODO code up instead of function or use heapq push pop
    return nlargest(k, result_dict, key = result_dict.get)
            
import Levenshtein #external package
from operator import itemgetter 
def suggest_v2(name, handles, k):
    result_dict = {}
    for handle in handles:
        result_dict.update({handle: Levenshtein.distance(name, handle)})
    # TODO change to k smallest
    return dict(sorted(result_dict.items(), key = itemgetter(1))[:k])

# TODO look into L1 distance
# from sklearn.feature_extraction.text import CountVectorizer
# def suggest_v3(name, handles, k):
#     return CountVectorizer.fit_transform(handles)

name = 'iLoveDogs'
handles = ['DogeCoin', 'YangGang2020', 'HodlForLife', 'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust']
# print("should return   ['GodIsLove', 'DogeCoin']", suggest(name, handles, k=2))
print("should return   ['GodIsLove', 'DogeCoin']", suggest_v2(name, handles, k=2))
# print("should return   ['GodIsLove', 'DogeCoin']", suggest_v3(name, handles, k=2))