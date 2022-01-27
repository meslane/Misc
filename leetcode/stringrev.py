string = "string"

revstring = []

for i in range(len(string)):
    revstring.append(string[len(string) - i - 1])
    
print(''.join(revstring))