def isPal(string):
    string = list(string)
    for i in range(0, len(string)):
        if (string[i] != string[len(string) - 1 - i]):
            return False
            
    return True

string = input("s = ")

longest = ""
for i in range(1, len(string) + 1): #string size adjust
    for j in range(0, len(string)): #string iteration
        substr = string[j:j+i]
        if isPal(substr):
            if len(substr) > len(longest):
                longest = substr

print(longest)