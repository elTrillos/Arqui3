



import re
from os import error

def decimalToBinary(n):
    return bin(n).replace("0b", "")

def checkIfValid(varsToCheck, posibleVars):
    #print(varsToCheck)
    #print("aaaaaa",posibleVars)
    cantPar = 0
    cannPar = 0
    listOfVarss,cantPar,wherePar=deleteStuff(varsToCheck)
    #print(wherePar)
    if cantPar>1:
        return -1
    #print(listOfVarss)
    isIn=0
    for i in listOfVarss:
        for k in posibleVars:
            #print(i,k)
            if i==k:
                isIn+=1
                break
            if i[0]=="#":
                isIn+=1
                break
        if wherePar==1 and i=="1":   
            cannPar=1   
        elif wherePar==0 and  listOfVarss[0]=="1":
            cannPar=2  
        if isIn==0:
            #print("invalido")
            return -1,cantPar,wherePar,cannPar
        k=0
    #print(isIn,cantPar)
    if isIn<len(listOfVarss):
        #print("invalido")
        return -1,cantPar,wherePar,cannPar
    return isIn,cantPar,wherePar,cannPar




def deleteStuff(listOfThings):
    countPar=listOfThings.count("(")
    listOfThings=re.split(',',listOfThings)
    count=0
    wherePar=0
    #print(listOfThings)
    if listOfThings[0][0]=="(":
        wherePar=1
    
    for i in listOfThings:
        i=i.replace("(","")
        i=i.replace(")","")
        listOfThings[count]=i
        count+=1
    return listOfThings,countPar,wherePar

def openfile():
    readd = []
    fileToOpen = open("p3-ej_incorrecto.ass","r")
    line=fileToOpen.readlines()
    for i in line:
        readd.append(i.split())
    return readd

def parserChecker(currLinea,numOfIns,varList,failLista):
    
    
    if currLinea[0]=="MOV":
        Checker=checkIfValid(currLinea[1],varList)
        #print(currLine[1])
        #print(deleteStuff(currLine[1]))
        #print(checkIfValid(currLine[1],varList))
        if 0<=Checker[0]<=2 and Checker[1]<=1:
            pass
            #numOfIns+=1
        
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="ADD":
        Checker=checkIfValid(currLinea[1],varList)
        #print(checkIfValid(currLine[1],varList))
        if Checker[0]==2 and Checker[1]<=1 and Checker[2]==0 and Checker[3]==0:
            pass
            #numOfIns+=1
        elif Checker[0]==1 and Checker[1]<=1 and Checker[2]==1:
            pass
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
        
    elif currLinea[0]=="SUB":
        Checker=checkIfValid(currLinea[1],varList)
        if Checker[0]==2 and Checker[1]<=1 and Checker[2]==0 and Checker[3]==0:
            pass
            #numOfIns+=1
        elif Checker[0]==1 and Checker[1]<=1 and Checker[2]==1:
            pass
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="AND":
        Checker=checkIfValid(currLinea[1],varList)
        if Checker[0]==2 and Checker[1]<=1  and Checker[2]==0 and Checker[3]==0:
            pass
            #numOfIns+=1
        elif Checker[0]==1 and Checker[1]<=1 and Checker[2]==1:
            pass
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="OR":
        Checker=checkIfValid(currLinea[1],varList)
        if 0<=Checker[0]==2 and Checker[1]<=1 and Checker[2]==0 and Checker[3]==0:
            pass
            #numOfIns+=1
        elif Checker[0]==1 and Checker[1]<=1 and Checker[2]==1:
            pass
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="NOT":
        Checker=checkIfValid(currLinea[1],varList)
        if 0<=Checker[0]==2 and Checker[1]<=1 and Checker[2]==0 and Checker[3]==0:
            pass
            #numOfIns+=1
        elif Checker[0]==1 and Checker[1]<=1 and Checker[2]==1:
            pass
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="XOR":
        Checker=checkIfValid(currLinea[1],varList)
        if 0<=Checker[0]==2 and Checker[1]<=1 and Checker[2]==0 and Checker[3]==0:
            pass
            #numOfIns+=1
        elif Checker[0]==1 and Checker[1]<=1 and Checker[2]==1:
            pass
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="SHL":
        Checker=checkIfValid(currLinea[1],varList)
        if 0<=Checker[0]==2 and Checker[1]<=1 and Checker[2]==1:
            pass

        else:
            failLista.append([currLinea ,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="SHR":
        Checker=checkIfValid(currLinea[1],varList)
        if 0<=Checker[0]==2 and Checker[1]<=1 and Checker[2]==1:
            pass
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="INC":
        Checker=checkIfValid(currLinea[1],varList)
        if 0<=Checker[0]<=1 and Checker[1]<=1 and Checker[2]==1:
            pass
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="RST":
        Checker=checkIfValid(currLinea[1],varList)
        if 0<=Checker[0]<=1 and Checker[1]<=1 and Checker[2]==1:
            pass
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="CMP":
        Checker=checkIfValid(currLinea[1],varList)
        if 0<=Checker[0]<=2 and Checker[1]<=1 and Checker[2]==0 and Checker[3]==0:
            pass
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="JMP":
        Checker=checkIfValid(currLinea[1],varList)
        #print(Checker)
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            pass
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="JEQ":
        Checker=checkIfValid(currLinea[1],varList)
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            pass
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="JNE":
        Checker=checkIfValid(currLinea[1],varList)
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            pass
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="JGT":
        Checker=checkIfValid(currLinea[1],varList)
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            pass
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="JLT":
        Checker=checkIfValid(currLinea[1],varList)
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            pass
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="JGE":
        Checker=checkIfValid(currLinea[1],varList)
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            pass
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="JLE":
        Checker=checkIfValid(currLinea[1],varList)
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            pass
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="JCR":
        Checker=checkIfValid(currLinea[1],varList)
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            pass
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="JOV":
        Checker=checkIfValid(currLinea[1],varList)
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            pass
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="CALL":
        Checker=checkIfValid(currLinea[1],varList)
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            pass
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="RET":
        Checker=checkIfValid(currLinea[1],varList)
        if Checker[0]==0 and Checker[1]<1:
            pass
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="POP":
        Checker=checkIfValid(currLinea[1],varList)
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            pass
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="PUSH":
        Checker=checkIfValid(currLinea[1],varList)
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            pass
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    else:
        failLista.append([currLinea,numOfIns])
        print("Error instruccion n: ",numOfIns)
        print("Instruccion no existe")
        print(currLinea)
    return failLista



def parser(fileList):
    nuList = []
    propList = []
    varList = []
    failList = []
    k = 1  #k=0  si se esta probando con CODE:############################################ 
    #print(dataParser(fileList))
    varDict = dataParser(fileList)
    #print("asdjasdjask")
    #print(varDict)
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
    varList.append("0")
    varList.append("1")
    #print("aaaaaa",propList)
    for i in propList:
        i=i.replace(":","")
        varList.append(i)
    #print("bbbbbb",varList)
    #print(varList)
    k = 1  #k=0  si se esta probando con CODE:############################################ 
    numOfIns=0
    #print(fileList)
    for currLine in fileList:
        #print(currLine)
        if currLine[0]=="CODE:":
            k=1
            continue
        elif currLine[0][-1]!=":" and k==1:
            
            nuList.append(currLine[0])
            #print(currLine)
            checc = parserChecker(currLine,numOfIns,varList,failList)
            #print("coomer",parserChecker(currLine,numOfIns,varList,failList))
            if checc:
                failList.append(checc)
            numOfIns+=1
        elif k==1 and currLine[0][-1]!=":":
            lineCheck = currLine.copy()
            lineCheck.pop(0)
            checc = parserChecker(lineCheck,numOfIns,varList,failList)
            if checc:
                failList.append(checc)
            numOfIns+=1
            #propList.append(currLine[0])
        

    k+=1
    #print(nuList)
    
    if len(failList)==0:
        print("Todo correcto, codigo funcional")
    #print(failList)
    return failList




def dataParser(fileList):
    dataList = {}
    defVars= []
    k=0
    if(fileList[0][0]!="DATA:"):
        #print("error")
        return []
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
                if currLine[1][0]=="#" :
                    if currLine[1].count("#") == 1:
                        currLine[1] = currLine[1].replace('#','')
                        currLine[1]=int(currLine[1],16)
                        currLine[1] = decimalToBinary(int(currLine[1]))
                        dataList[currLine[0]]=currLine[1]
                        defVars.append(currLine[0])
                    else:
                        print("Error formato hexadecimal:",currLine[1])
                        
                else:
                    currLine[1] = decimalToBinary(int(currLine[1]))
                    dataList[currLine[0]]=currLine[1]
                    defVars.append(currLine[0])
                #print(dataList)
    
    return dataList



    

fileee = openfile()

#print(fileee)
#print(dataParser(fileee))
#print(dataParser(fileee))
parser(fileee)