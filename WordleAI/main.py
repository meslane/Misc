import random

def cullWords(words, grey, yellow, green):
    for word in list(words):
        culled = False
    
        for char in yellow: #cull words not containing yellows
            if char not in word:
                words.remove(word)
                culled = True
                break
        
        if not culled:
            for i, char in enumerate(word):
                if (char in grey) and (char != green[i]):
                    words.remove(word)
                    break
                    
                if green[i] != 0:
                    if char != green[i]:
                        words.remove(word)
                        break
                    
                if char in yellow: #if key exists in dict
                    if i in yellow[char]: #if index of char is in list of forbidden positions
                        words.remove(word)
                        break
                
def main():
    words = []
    with open("fiveletters.txt") as f:
        words = f.read().split()
        
    openers = ["adieu", "among", "audio", "equal", "ratio", "stain", "irate", "stare", "arise", "roast"]

    greys = [] #list of chars not in word
    yellows = {} #dict of chars in word but not in right place
    greens = [0, 0, 0, 0, 0] #list of chars in word and in right place
    
    for l in range(0, 7):
        try:
            if (l == 0):
                currentWord = openers[random.randint(0, len(openers) - 1)]
            else:
                currentWord = words[random.randint(0, len(words) - 1)]
        except ValueError:
            print("I ran out of words, I lose :(")
            break
            
        print("{} (pool size = {})".format(currentWord, len(words)))
        
        check = input().lower()[0:5]
        
        if check == "ggggg":
            print("I win!")
            break
        elif l == 5:
            print("I lose :(")
            break
        
        for i, char in enumerate(check): #scan input and append to respective lists/dicts
            if char == 'g':
                #if currentWord[i] in greys:
                    #greys.remove(currentWord[i]) #remove if put in greys first
                greens[i] = currentWord[i]
            elif char == 'y':
                if currentWord[i] not in yellows:
                    yellows[currentWord[i]] = [i]
                else:
                    yellows[currentWord[i]].append(i)
            else:
                if (currentWord[i] not in yellows): #prevent double insertion
                    greys.append(currentWord[i])
                    
        words.remove(currentWord)
        cullWords(words, greys, yellows, greens)

if __name__ == "__main__":
    main()