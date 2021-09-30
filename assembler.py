




from os import error

def decimalToBinary(n):
    return bin(n).replace("0b", "")

def openfile():
    readd = []
    fileToOpen = open("p3F_1.ass","r")
    line=fileToOpen.readlines()
    for i in line:
        readd.append(i.split())
    return readd


def parser(fileList):
    nuList = []
    propList = []
    k = 0
        
    print(fileList[k][0])
    for currLine in fileList:
        
        if currLine[0]=="CODE:":
            k=1
            continue
        elif currLine[0][-1]!=":" and k==1:
            #print("yeet")
            nuList.append(currLine[0])
        elif k==1:
            propList.append(currLine[0])
    k+=1
            
    return nuList 











def dataParser(fileList):
    dataList = {}
    k=0
    if(fileList[0][0]!="DATA:"):
        print("error")
        return 0
    elif(fileList[0][0]=="DATA:"):
        #print("chupalo")
        for currLine in fileList:
            #print(currLine)
            if currLine[0]=="CODE:":
                return dataList
            elif len(currLine)!=2 and currLine[0]!="DATA:" :
                continue
            elif len(currLine)==2:
                #print("adasdasdlkjasd")
                if currLine[1][0]=="#":
                    currLine[1] = currLine[1].replace('#','')
                    currLine[1]=int(currLine[1],16)
                currLine[1] = decimalToBinary(int(currLine[1]))
                dataList[currLine[0]]=currLine[1]
                #print(dataList)

    return dataList



    

fileee = openfile()

print(fileee)
print(dataParser(fileee))
print(parser(fileee))