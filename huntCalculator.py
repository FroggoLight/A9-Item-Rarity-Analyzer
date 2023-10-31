

def writeData(fileName, newData):
    dataFile = open(fileName, "a")
    dataFile.write(newData + "\n")
    dataFile.close()


def calculateData(fileName):
    dataFile = open(fileName, "r")
    dataList = dataFile.readlines()
    dataFile.close()
    
    dataDict = {
        "2k" : 0,
        "4k" : 0,
        "ct" : 0,
        "ca" : 0,
        "ch" : 0,
        "cn" : 0,
        "rt" : 0,
        "ra" : 0,
        "rh" : 0,
        "rn" : 0,
        "bp" : 0
        }
    validItemCount = 0
    
    for line in dataList:
        items = line.replace("\n", "").split()
        for item in items:
            if dataDict.get(item.lower(), "Not Found") != "Not Found":
                dataDict[item] += 1
                validItemCount += 1
    
    dictKeys = list(dataDict.keys())
    for key in dictKeys:
        itemWeight = dataDict[key] / validItemCount * 100
        print(f"{key} Weight: {itemWeight:.2f}%")
    #bpRate = dataDict["bp"] / validItem * 100
    #calprint(f"Blueprint Weight: {bpRate:.2f}%")
            


running = True
while running:
    print("input action")
    action = input()
    if action == "quit":
        running = False
    if action == "add":
        print("Selections:")
        huntData = input()
        writeData("huntData.txt", huntData)
    if action == "calculate":
        calculateData("huntData.txt")
        
## 2k - 2000 credits
## 4k - 4000 credits
## ct - Common TS import
## ca - Common Accel import
## ch - Common Handling import
## cn - Common Nitro import
## rt - Rare TS import
## ra - Rare Accel import
## rh - Rare Handling import
## rn - Rare Nitro import
## bp - Blueprint