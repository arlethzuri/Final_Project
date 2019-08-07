# Creates a dictionary to store values
dictionary = {}

# Creates a dictionary for the anagrams with more than one word inside
ana_dict = {}

# =====================================
#       INPUTS
# =====================================

# Prompts a word from user (program will search for anagrams of the word)
user = input("Search for anagrams of: ")
user_key = ''.join(sorted(user))

ana_dict_key = eval(input("Anagram Dictionary Key: "))

# =====================================
#       DICTIONARY MAKERS AND SORTING
# =====================================

# Opens the abr_dict.txt file
# Create dictionary keys and setting their values equal to []
with open('abr_dict.txt','r') as abr_dict:
    for w in abr_dict:
        w_str = w.strip('\n')
        key = ''.join(sorted(w_str))
        dictionary[key] = []

with open('abr_dict.txt','r') as abr_dict:
    for w in abr_dict:
        w_str = w.strip('\n')
        key = ''.join(sorted(w_str))
        dictionary[key].append(w_str)

for dict_value in dictionary.values():
    if len(dict_value) > 1:
        ana_dict[len(dict_value)] = []

for dict_key, dict_value in dictionary.items():
    if len(dict_value) > 1:
        ana_dict[len(dict_value)].append(dict_value)

# Order the sublists inside a list (value from ana_dict) based on string length of first elements
# key = lambda l: len(l[0]) ==> call each element (in our case, sublist) as l
#                           ==> determine length of first string in l
for dict_value in ana_dict.values():
    dict_value.sort(key = lambda l:len(l[0]))

# =====================================
#       OUTPUTS
# =====================================

# Prints the list of anagrams for word inputted by user
print(dictionary[user_key])

# Prints the anagram dictionary values for the key value (i.e. 2, 3, 4, 5, etc.)
print(ana_dict[ana_dict_key])



# Objectives:
# ===========================
# 1. Pick out all the keys that have more than one anagram.
# 2. Order the keys; keys with two elements are first, the keys with most elements are last.
# 3. Within keys with same number of elements, sort by how long their anagrams are.
# 4. Write a way that can pull the most interesting sets


# Special Function Ideas:
# ===========================
# 1. How similar it is to its alphabetized key
# 2. If the anagram key has a word where its letters are already alphabetized
