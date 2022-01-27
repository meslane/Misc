#sort all words in dict and grab only those with 5 letters that are not proper nouns

f = open("words.txt")
words = f.read().split()

with open("fiveletters.txt", 'w') as fl:
    for word in words:
        if (len(word) == 5 and "'" not in word and not word[0].isupper()):
            fl.write(word + '\n')