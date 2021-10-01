



import re
from os import error

def decimalToBinary(n):
    return bin(n).replace("0b", "")

def checkIfValid(varsToCheck, posibleVars):
    #print(varsToCheck)
    cantPar = 0
    listOfVarss,cantPar=deleteStuff(varsToCheck)
    if cantPar>1:
        return -1
    #print(listOfVarss)
    isIn=0
    for i in listOfVarss:
        for k in posibleVars:
            print(i,k)
            if i==k:
                isIn+=1
                break
                
        if isIn==0:
            print("invalido")
            return -1,cantPar
        k=0
    #print(isIn,cantPar)
    return isIn,cantPar




def deleteStuff(listOfThings):
    countPar=listOfThings.count("(")
    listOfThings=re.split(',',listOfThings)
    count=0
    
    for i in listOfThings:
        i=i.replace("(","")
        i=i.replace(")","")
        listOfThings[count]=i
        count+=1
    return listOfThings,countPar

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
    varList = []
    k = 0
    #print(dataParser(fileList))
    varDict = dataParser(fileList)
    #print("asdjasdjask")
    for i in varDict:
        varList.append(i)
    #print(varList)
    #print(fileList[k][0])
    for currLain in fileList:
        if currLain[0]=="CODE:":
            k=1
            continue
        elif currLain[0][-1]==":" and k==1:
            propList.append(currLain[0])
    #print(propList)
    varList.append("A")
    varList.append("B")
    varList.append("Dir")
    print("aaaaaa",propList)
    for i in propList:
        i=i.replace(":","")
        varList.append(i)
    print("bbbbbb",varList)
    #print(varList)
    k = 0
    numOfIns=0
    for currLine in fileList:
        #print(currLine)
        if currLine[0]=="CODE:":
            k=1
            continue
        elif currLine[0][-1]!=":" and k==1:
            nuList.append(currLine[0])
            print(currLine)
            if currLine[0]=="MOV":
                print(currLine[1])
                #print(deleteStuff(currLine[1]))
                #print(checkIfValid(currLine[1],varList))
                if 0<=checkIfValid(currLine[1],varList)[0]<=2 and checkIfValid(currLine[1],varList)[1]<=1:
                    numOfIns+=1
                else:
                    print(" error",numOfIns)
                    return nuList
            elif currLine[0]=="ADD":
                print(checkIfValid(currLine[1],varList))
                if 0<=checkIfValid(currLine[1],varList)[0]<=2 and checkIfValid(currLine[1],varList)[1]<=1:
                    numOfIns+=1
                else:
                    print(" error",numOfIns)
                    return nuList
                
            elif currLine[0]=="SUB":
                if 0<=checkIfValid(currLine[1],varList)[0]<=2 and checkIfValid(currLine[1],varList)[1]<=1:
                    numOfIns+=1
                else:
                    print(" error",numOfIns)
                    return nuList
            elif currLine[0]=="AND":
                if 0<=checkIfValid(currLine[1],varList)[0]<=2 and checkIfValid(currLine[1],varList)[1]<=1:
                    numOfIns+=1
                else:
                    print(" error",numOfIns)
                    return nuList
            elif currLine[0]=="OR":
                if 0<=checkIfValid(currLine[1],varList)[0]<=2 and checkIfValid(currLine[1],varList)[1]<=1:
                    numOfIns+=1
                else:
                    print(" error",numOfIns)
                    return nuList
            elif currLine[0]=="NOT":
                if 0<=checkIfValid(currLine[1],varList)[0]<=2 and checkIfValid(currLine[1],varList)[1]<=1:
                    numOfIns+=1
                else:
                    print(" error",numOfIns)
                    return nuList
            elif currLine[0]=="XOR":
                if 0<=checkIfValid(currLine[1],varList)[0]<=2 and checkIfValid(currLine[1],varList)[1]<=1:
                    numOfIns+=1
                else:
                    print(" error",numOfIns)
                    return nuList
            elif currLine[0]=="SHL":
                if 0<=checkIfValid(currLine[1],varList)[0]<=2 and checkIfValid(currLine[1],varList)[1]<=1:
                    numOfIns+=1
                else:
                    print(" error",numOfIns)
                    return nuList
            elif currLine[0]=="SHR":
                if 0<=checkIfValid(currLine[1],varList)[0]<=2 and checkIfValid(currLine[1],varList)[1]<=1:
                    numOfIns+=1
                else:
                    print(" error",numOfIns)
                    return nuList
            elif currLine[0]=="INC":
                if 0<=checkIfValid(currLine[1],varList)[0]<=2 and checkIfValid(currLine[1],varList)[1]<=1:
                    numOfIns+=1
                else:
                    print(" error",numOfIns)
                    return nuList
            elif currLine[0]=="RST":
                if 0<=checkIfValid(currLine[1],varList)[0]<=2 and checkIfValid(currLine[1],varList)[1]<=1:
                    numOfIns+=1
                else:
                    print(" error",numOfIns)
                    return nuList
            elif currLine[0]=="CMP":
                if 0<=checkIfValid(currLine[1],varList)[0]<=2 and checkIfValid(currLine[1],varList)[1]<=1:
                    numOfIns+=1
                else:
                    print(" error",numOfIns)
                    return nuList
            elif currLine[0]=="JMP":
                if 0<=checkIfValid(currLine[1],varList)[0]<=2 and checkIfValid(currLine[1],varList)[1]<=1:
                    numOfIns+=1
                else:
                    print(" error",numOfIns)
                    return nuList
            elif currLine[0]=="JEQ":
                if 0<=checkIfValid(currLine[1],varList)[0]<=2 and checkIfValid(currLine[1],varList)[1]<=1:
                    numOfIns+=1
                else:
                    print(" error",numOfIns)
                    return nuList
            elif currLine[0]=="JNE":
                if 0<=checkIfValid(currLine[1],varList)[0]<=2 and checkIfValid(currLine[1],varList)[1]<=1:
                    numOfIns+=1
                else:
                    print(" error",numOfIns)
                    return nuList
            elif currLine[0]=="JGT":
                if 0<=checkIfValid(currLine[1],varList)[0]<=2 and checkIfValid(currLine[1],varList)[1]<=1:
                    numOfIns+=1
                else:
                    print(" error",numOfIns)
                    return nuList
            elif currLine[0]=="JLT":
                if 0<=checkIfValid(currLine[1],varList)[0]<=2 and checkIfValid(currLine[1],varList)[1]<=1:
                    numOfIns+=1
                else:
                    print(" error",numOfIns)
                    return nuList
            elif currLine[0]=="JGE":
                if 0<=checkIfValid(currLine[1],varList)[0]<=2 and checkIfValid(currLine[1],varList)[1]<=1:
                    numOfIns+=1
                else:
                    print(" error",numOfIns)
                    return nuList
            elif currLine[0]=="JLE":
                if 0<=checkIfValid(currLine[1],varList)[0]<=2 and checkIfValid(currLine[1],varList)[1]<=1:
                    numOfIns+=1
                else:
                    print(" error",numOfIns)
                    return nuList
            elif currLine[0]=="JCR":
                if 0<=checkIfValid(currLine[1],varList)[0]<=2 and checkIfValid(currLine[1],varList)[1]<=1:
                    numOfIns+=1
                else:
                    print(" error",numOfIns)
                    return nuList
            elif currLine[0]=="JOV":
                if 0<=checkIfValid(currLine[1],varList)[0]<=2 and checkIfValid(currLine[1],varList)[1]<=1:
                    numOfIns+=1
                else:
                    print(" error",numOfIns)
                    return nuList
            else:
                return 0
        elif k==1:
            continue
            #propList.append(currLine[0])

    k+=1
    #print(nuList)
    

    print(fileList)
    return numOfIns 




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
    
    return dataList



    

fileee = openfile()

#print(fileee)
#print(dataParser(fileee))
print(dataParser(fileee))
print(parser(fileee))