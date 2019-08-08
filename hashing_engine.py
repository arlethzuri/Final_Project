# =====================================
#       SETUP OF PROGRAM
# =====================================
#Importing libraries
import os

# Creates a dictionary to store values
dictionary = {}

# Creates a dictionary for the anagrams with more than one word inside
ana_dict = {}

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
#       INPUTS and OUTPUTS
# =====================================
# Clears screen
os.system("clear")

# Introduction
print("================================================\n")
print("FINAL PROJECT: ANAGRAMS")
print("Arleth, Akwe, and Chen\n")
print("================================================\n")

# PART 1: ANAGRAM SEARCHER
# Prompts a word from user (program will search for anagrams of the word)
print("\nPart 1: Anagram Searcher")
print("================================================")
user = input("Search for anagrams of: ")
user_key = ''.join(sorted(user))
print("")

# Prints the list of anagrams for word inputted by user
print(dictionary[user_key])


#PART 2: SEARCH BASED ON ANAGRAM DICTIONARY KEY
print("\nPart 2: Anagram Dictionary Key Searching")
print("================================================")
print("Lists of anagrams have been grouped based on")
print("how many anagrams are associated with a word.")
print("This will search by the number of anagrams")
print("that are in a list of anagrams.")
print("================================================")
ana_dict_key = eval(input("Anagram Dictionary Key: "))

# Prints the anagram dictionary values for the key value (i.e. 2, 3, 4, 5, etc.)
os.system("clear")
print(ana_dict[ana_dict_key])


# =====================================
#       INTERESTING SEARCHERS
# =====================================

# FUNCTION 1: Rotation Searcher (Basic)

# This will go into a specific key (i.e. 2, 3, 4, 5, etc.) of ana_dict and
# search for words that are rotations of each other

print("\n\nFunction 1: Rotation Searcher")
print("================================================")
print("This will take in anagram dictionary keys.")
print("These keys are like before (i.e. 2, 3, 4, etc.)")
print("A rotation is done by moving a word's first")
print("letter to the end of the word.")
print("If a word's rotation is also an anagram, then")
print("we have a valid pair.")

new_key = eval(input("Key Number: "))
for sub_list in ana_dict[new_key]:
    for string in sub_list:
        value = True
        temp_str = string[1:] + string[0]
        if temp_str in sub_list:
            print(string, temp_str)


# FUNCTION 2: Rotation Searcher (Stricter)

# This will also go into a specific key (i.e. 2, 3, 4, 5, etc.) of ana_dict and
# search for sublists whose elements are all rotations of each other

print("\n\nFunction 2: Rotation Searcher (Stricter)")
print("================================================")
print("This is like Function 1, except that we only")
print("want lists where all its anagrams and their")
print("rotations exist in the list.")
new_key = eval(input("Key Number: "))
for sub_list in ana_dict[new_key]:
    for string in sub_list:
        value = True
        temp_str = string[1:] + string[0]
        if temp_str not in sub_list:
            value = False
            break
    if value == True:
        print(sub_list)


# FUNCTION 3: Word Transpositions

# This will also go into a specific key (i.e. 2, 3, 4, 5, etc.) of ana_dict and
# search for word pairs where they are different only the switching of two
# adjacent characters in their strings.

print("\n\nFunction 3: Word Transpositions")
print("================================================")
print("A transposition is the swapping of two adjacent")
print("letters in word.")
print("This function will search for pairs of anagrams")
print("that are transpositions of each other.")
new_key = eval(input("Key Number: "))
for sub_list in ana_dict[new_key]:
    for string in sub_list:
        for i in range(1,len(string)):
            new_string = string[:i-1] + string[i] + string[i-1] + string[i+1:]
        if new_string != string and (new_string in sub_list):
            print(string,new_string)

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
# 3. Rotation of letters (push first to the back, check it it exists)
# 4. An extreme case of 3: all anagrams are rotations of each other
