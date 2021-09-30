



import re
from os import error

def decimalToBinary(n):
    return bin(n).replace("0b", "")

def checkIfValid(varsToCheck, posibleVars):
    
    print(posibleVars)
    isIn=0
    for i in varsToCheck:
        for k in posibleVars:
            print(i,k)
            if i==k:
                isIn+=1
                break
                
        if isIn==0:
            print("invalido")
            return 0
        k=0
    return 1




def deleteStuff(listOfThings):
    listOfThings=re.split(',',listOfThings)
    count=0
    for i in listOfThings:
        i=i.replace("(","")
        i=i.replace(")","")
        listOfThings[count]=i
        count+=1
    return listOfThings

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
    #print(dataParser(fileList))
    varsUsed = dataParser(fileList)[1]
    #print(fileList[k][0])
    for currLain in fileList:
        if currLain[0]=="CODE:":
            k=1
            continue
        elif currLain[0][-1]==":" and k==1:
            propList.append(currLain[0])
    #print(propList)
    propList.append("A")
    propList.append("B")
    propList.append("Dir")
    k = 0
    numOfIns=0
    for currLine in fileList:
        #print(currLine)
        if currLine[0]=="CODE:":
            k=1
            continue
        elif currLine[0][-1]!=":" and k==1:
            nuList.append(currLine[0])
            #print(currLine[0])
            if currLine[0]=="MOV":
                #print(currLine[1])
                print(deleteStuff(currLine[1]))
                print(checkIfValid(deleteStuff(currLine[1]),varsUsed))
                #print(currLine[1])
                continue
            elif currLine[0]=="ADD":
                continue
            elif currLine[0]=="SUB":
                continue
            elif currLine[0]=="AND":
                continue
            elif currLine[0]=="OR":
                continue
            elif currLine[0]=="NOT":
                continue
            elif currLine[0]=="XOR":
                continue
            elif currLine[0]=="SHL":
                continue
            elif currLine[0]=="SHR":
                continue
            elif currLine[0]=="INC":
                continue
            elif currLine[0]=="RST":
                continue
            elif currLine[0]=="CMP":
                continue
            elif currLine[0]=="JMP":
                continue
            elif currLine[0]=="JEQ":
                continue
            elif currLine[0]=="JNE":
                continue
            elif currLine[0]=="JGT":
                continue
            elif currLine[0]=="JLT":
                continue
            elif currLine[0]=="JGE":
                continue
            elif currLine[0]=="JLE":
                continue
            elif currLine[0]=="JCR":
                continue
            elif currLine[0]=="JOV":
                continue
            else:
                return 0
        elif k==1:
            continue
            #propList.append(currLine[0])

    k+=1
    #print(nuList)
    

    print(fileList)
    return nuList 




def dataParser(fileList):
    dataList = {}
    defVars= []
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
                defVars.append(currLine[0])
                #print(dataList)

    return [dataList,defVars]



    

fileee = openfile()

#print(fileee)
#print(dataParser(fileee))
print(dataParser(fileee))
print(parser(fileee))