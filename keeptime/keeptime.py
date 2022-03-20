import time
import datetime
import json
import math

startTime = 0

while True:
    cmd = input(">").lower()
    
    if (startTime != 0 and (cmd == "total" or cmd == "exit")):
        print("WARNING: time is currently being counted, use the 'end' or 'save' command to potentially avoid losing recorded time")
        cmd = "reject"
    
    if (cmd == "start"):
        if (startTime == 0):
            startTime = time.time()
            print("Beginning time accounting")
        else:
            print("ERROR: time is alredy being counted")
            
    elif (cmd == "end" or cmd == "save"):
        if (startTime != 0):
            total = int(time.time() - startTime)
            
            try:
                with open("timecard.json", 'r') as j:
                    table = json.load(j)
            except json.decoder.JSONDecodeError:
                print("Error opening file, creating blank table")
                table = {}
            
            date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
            
            if date not in table:
                table[date] = total
            else:
                table[date] = int(table[date]) + total
              
            with open("timecard.json", 'w') as j:
                json.dump(table, j, indent=4)
            
            if (cmd == "end"):
                startTime = 0
            elif (cmd == "save"):
                startTime = time.time()
            
            print("Saved time to file")
        else:
            print("ERROR: time is not being counted")
            
    elif (cmd == "total"):
        startSearch = input("Input start date:")
        endSearch = input("Input end date:")
        
        with open("timecard.json", 'r') as j:
            table = json.load(j)
        
        sum = 0
        keyList = list(table.keys())
        try:
            for key in keyList[keyList.index(startSearch):keyList.index(endSearch)+1]:
                sum += int(table[key])
                
            #print(time.strftime("%Hh %Mm %Ss", time.gmtime(sum)))
            print("{}h {}m {}s".format(math.floor(sum/3600), math.floor((sum / 60) % 60), (sum % 60)))
            
            rate = input("Enter rate: $")
            
            print("Pay = ${:0.2f}".format(sum * (float(rate)/3600)))
        except ValueError:
            print("ERROR: one or more of the entered dates is not in the list")
                
    elif (cmd == "exit"):
        break