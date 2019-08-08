# Program removes words with less than 8 characters from the dictionary
# Program then writes words that have at least 8 characters into a new txt file

with open('eng_dict.txt','r') as infile:
    with open('abr_dict.txt','w') as outfile:
        for line in infile:
            if len(line) >= 9:
                line = line.lower()
                outfile.write(line)
