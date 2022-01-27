pattern = input("pattern = ")
string = input("s = ")

pdict = {}

pattern = list(pattern)
string = string.split()
   
pindex = 0
i = 0
match = 1
for s in string:
    if s not in pdict:
        if pindex < len(pattern):
            pdict[s] = pattern[pindex]
            pindex += 1
        else:
            match = 0
            break
    
    if i >= len(pattern) or pdict[s] != pattern[i]:
        match = 0
        break
        
    i += 1
    
    
if match == 1:
    print("true")
else:
    print("false")