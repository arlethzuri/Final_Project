with open('eng_dict.txt','r') as infile:
    with open('abr_dict.txt','w') as outfile:
        for line in infile:
            if len(line) >= 9:
                line = line.lower()
                outfile.write(line)
