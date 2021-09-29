




from os import error


def openfile():
    readd = []
    fileToOpen = open("p3F_1.ass","r")
    line=fileToOpen.readlines()
    for i in line:
        readd.append(i.split())
    return readd


def parser(line):
    return 0

def dataParser(fileList):
    dataList = {}
    k=0
    if(fileList[0][0]!="DATA:"):
        return 0
    elif(fileList[0][0]=="DATA:"):
        #print("chupalo")
        for currLine in fileList:
            #print(currLine)
            if currLine[0]=="CODE:":
                continue
            elif len(currLine)!=2 and currLine[0]!="DATA:" :
                continue
            elif len(currLine)==2:
                #print("adasdasdlkjasd")
                if currLine[1][0]=="#":
                    currLine[1] = currLine[1].replace('#','')
                dataList[currLine[0]]=currLine[1]
                #print(dataList)

    return dataList



    

fileee = openfile()

print(fileee)
print(dataParser(fileee))