



import re
from os import error

def checkHex(s): #Obtenido y modificado de 
    #print(s[0])
    if s[0]!="#":
        return -1
    else:
        #print("aaa")
        s=s.replace("#",'')
    #print(s)
    for ch in s:
        if ((ch < '0' or ch > '9') and
            (ch < 'A' or ch > 'F')):   
            return -1

    sval=int(s,16)
    #print(sval)
    if sval>255:
        return -1
    else: 
        return sval
def decimalToBinary(n):
    binn = bin(n).replace("0b", "")
    x= binn[::-1]
    while len(x)<8:
        x+='0'
    
    return x[::-1]

def printStuffToFile(listOfArgs,varDictToCheckk ,varDataDictToCheckk,tagsDictToCheckk,mode,varDataDataCheckk,outFile):
    #print("asdwww",varDataDictToCheckk)
    #print("asdaw",varDataDataCheckk)
    #print("asdawas",tagsDictToCheckk)
    countt=0
    #listOfArgs="lista"
    #print(listOfArgs)
    if listOfArgs in varDataDictToCheckk and mode == 1:
        print("111",varDataDictToCheckk[listOfArgs])
        outFile.write(decimalToBinary(varDataDictToCheckk[listOfArgs]))
    if listOfArgs in varDataDataCheckk and mode == 2:
        print("222",varDataDataCheckk[listOfArgs])
        outFile.write(decimalToBinary(varDataDataCheckk[listOfArgs]))
    if listOfArgs in tagsDictToCheckk and mode == 3:
        print("333",tagsDictToCheckk[listOfArgs])
        outFile.write(decimalToBinary(tagsDictToCheckk[listOfArgs]))
    outFile.write("\n")
    countt+=1


def checkIfValid(varsToCheck, posibleVars):
    #print(varsToCheck)
    #print("aaaaaa",posibleVars)
    cantPar = 0
    cannPar = 0
    listOfVarss,cantPar,wherePar=deleteStuff(varsToCheck)
    #print(wherePar)
    if cantPar>1:
        return -1,cantPar,wherePar,cannPar
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
            #print(k[0])
            if k[0].isalpha():
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
    fileToOpen = open("p3F_1.ass","r")
    line=fileToOpen.readlines()
    for i in line:
        readd.append(i.split())
    return readd

def parserChecker(currLinea,numOfIns,varList,failLista,outFileee,litListt,varDictt,litDictt,varDataDictt,varDataLocDictt):
    Checker=checkIfValid(currLinea[1],varList)
    lineToCheckk=deleteStuff(currLinea[1])[0]
    #print("bb",varDataDictt)
    #print("kk", litDictt)
    #print(lineToCheckk)
    #print(Checker)
    if currLinea[0]=="MOV":
        #print(currLinea)
        if Checker[0]==2 and Checker[1]==0:
            if lineToCheckk[0]=="A" and lineToCheckk[1]=="B":
                #print("bb",varDataDictt)
                #print("kk", litDictt)
                #printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,1)
                outFileee.write("0000000\n")
            elif lineToCheckk[0]=="B" and lineToCheckk[1]=="A":
                outFileee.write("0000001\n")
            elif lineToCheckk[0]=="A" and lineToCheckk[1] in litListt:
                outFileee.write("0000010 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,2,varDataLocDictt,outFileee)
            elif lineToCheckk[0]=="B" and lineToCheckk[1] in litListt:
                outFileee.write("0000011 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,2,varDataLocDictt,outFileee)
        elif Checker[0]==2 and Checker[1]==1:
            if Checker[2]==0:
                if lineToCheckk[0]=="A" and lineToCheckk[1] in litListt:
                    outFileee.write("0100101 ")
                    printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
                elif lineToCheckk[0]=="B" and lineToCheckk[1] in litListt:
                    outFileee.write("0100110 ")
                    printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
                elif lineToCheckk[0]=="A" and lineToCheckk[1]=="B":
                    outFileee.write("0101001\n")
                elif lineToCheckk[0]=="B" and lineToCheckk[1]=="B":
                    outFileee.write("0101010\n")
            elif Checker[2]==1:
                if lineToCheckk[1]=="A" and lineToCheckk[0] in litListt:
                    outFileee.write("0100111 ")
                    printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
                elif lineToCheckk[1]=="B" and lineToCheckk[0] in litListt:
                    outFileee.write("0101000 ")
                    printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
                elif lineToCheckk[1]=="A" and lineToCheckk[0]=="B":
                    outFileee.write("0101011\n")
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="ADD":
        lineToCheckk=deleteStuff(currLinea[1])[0]
        #print(lineToCheckk)
        #print(checkIfValid(currLine[1],varList))
        if Checker[0]==2 and Checker[1]==0:
            if lineToCheckk[0]=="A" and lineToCheckk[1]=="B":
                outFileee.write("0000100\n")
            elif lineToCheckk[0]=="B" and lineToCheckk[1]=="A":
                outFileee.write("0000101\n")
            elif lineToCheckk[0]=="A" and lineToCheckk[1] in litListt:
                outFileee.write("0000110 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,2,varDataLocDictt,outFileee)
            elif lineToCheckk[0]=="B" and lineToCheckk[1] in litListt:
                outFileee.write("0000111 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,2,varDataLocDictt,outFileee)
            #numOfIns+=1
        elif Checker[0]==2 and Checker[1]==1 and Checker[2]==0 and Checker[3]==0:
            if lineToCheckk[0]=="A" and lineToCheckk[1] in litListt:
                outFileee.write("0101100 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
            elif lineToCheckk[0]=="B" and lineToCheckk[1] in litListt:
                outFileee.write("0101101 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
            elif lineToCheckk[0]=="A" and lineToCheckk[1]=="B":
                outFileee.write("0101110\n")
        elif Checker[0]==1 and Checker[1]==1 and Checker[2]==1 and Checker[3]==0:
            if lineToCheckk[0] in litListt:
                outFileee.write("0101111 ")
                printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
        
    elif currLinea[0]=="SUB":
        lineToCheckk=deleteStuff(currLinea[1])[0]
        #print(lineToCheckk)
        if Checker[0]==2 and Checker[1]==0:
            if lineToCheckk[0]=="A" and lineToCheckk[1]=="B":
                outFileee.write("0001000\n")
            elif lineToCheckk[0]=="B" and lineToCheckk[1]=="A":
                outFileee.write("0001001\n")
            elif lineToCheckk[0]=="A" and lineToCheckk[1] in litListt:
                outFileee.write("0001010 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,2,varDataLocDictt,outFileee)
            elif lineToCheckk[0]=="B" and lineToCheckk[1] in litListt:  
                outFileee.write("0001011 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,2,varDataLocDictt,outFileee)
            #numOfIns+=1
        elif Checker[0]==2 and Checker[1]==1 and Checker[2]==0 and Checker[3]==0:
            if lineToCheckk[0]=="A" and lineToCheckk[1] in litListt:
                outFileee.write("0110000 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
            elif lineToCheckk[0]=="B" and lineToCheckk[1] in litListt:
                outFileee.write("0110001 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
            elif lineToCheckk[0]=="A" and lineToCheckk[1]=="B":
                outFileee.write("0110010\n")
                #printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,1,varDataLocDictt)
        elif Checker[0]==1 and Checker[1]==1 and Checker[2]==1 and Checker[3]==0:
            if lineToCheckk[0] in litListt:
                outFileee.write("0110011 ")
                printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="AND":
        lineToCheckk=deleteStuff(currLinea[1])[0]
        #print(lineToCheckk)
        if Checker[0]==2 and Checker[1]==0:
            if lineToCheckk[0]=="A" and lineToCheckk[1]=="B":
                outFileee.write("0001100\n")
            elif lineToCheckk[0]=="B" and lineToCheckk[1]=="A":
                outFileee.write("0001101\n")
            elif lineToCheckk[0]=="A" and lineToCheckk[1] in litListt:
                outFileee.write("0001110 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,2,varDataLocDictt,outFileee)
            elif lineToCheckk[0]=="B" and lineToCheckk[1] in litListt:
                outFileee.write("0001111 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,2,varDataLocDictt,outFileee)
            #numOfIns+=1
        elif Checker[0]==2 and Checker[1]==1 and Checker[2]==0 and Checker[3]==0:
            if lineToCheckk[0]=="A" and lineToCheckk[1] in litListt:
                outFileee.write("0110100 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
            elif lineToCheckk[0]=="B" and lineToCheckk[1] in litListt:
                outFileee.write("0110101 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
            elif lineToCheckk[0]=="A" and lineToCheckk[1]=="B":
                outFileee.write("0110110\n")
        elif Checker[0]==1 and Checker[1]==1 and Checker[2]==1 and Checker[3]==0:
            if lineToCheckk[0] in litListt:
                outFileee.write("0110111 ")
                printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="OR":
        lineToCheckk=deleteStuff(currLinea[1])[0]
        #print(lineToCheckk)
        if Checker[0]==2 and Checker[1]==0:
            if lineToCheckk[0]=="A" and lineToCheckk[1]=="B":
                outFileee.write("0010000\n")
            elif lineToCheckk[0]=="B" and lineToCheckk[1]=="A":
                outFileee.write("0010001\n")
            elif lineToCheckk[0]=="A" and lineToCheckk[1] in litListt:
                outFileee.write("0010010 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,2,varDataLocDictt,outFileee)
            elif lineToCheckk[0]=="B" and lineToCheckk[1] in litListt:
                outFileee.write("0010011 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,2,varDataLocDictt,outFileee)
            #numOfIns+=1
        elif Checker[0]==2 and Checker[1]==1 and Checker[2]==0 and Checker[3]==0:
            if lineToCheckk[0]=="A" and lineToCheckk[1] in litListt:
                outFileee.write("0111000 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
            elif lineToCheckk[0]=="B" and lineToCheckk[1] in litListt:
                outFileee.write("0111001 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
            elif lineToCheckk[0]=="A" and lineToCheckk[1]=="B":
                outFileee.write("0111010\n")

        elif Checker[0]==1 and Checker[1]==1 and Checker[2]==1 and Checker[3]==0:
            if lineToCheckk[0] in litListt:
                outFileee.write("0111011 ")
                printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="NOT":
        lineToCheckk=deleteStuff(currLinea[1])[0]
        #print(lineToCheckk)
        if Checker[0]==2 and Checker[1]==0:
            if lineToCheckk[0]=="A" and lineToCheckk[1]=="A":
                outFileee.write("0010100\n")
            elif lineToCheckk[0]=="B" and lineToCheckk[1]=="A":
                outFileee.write("0010110\n")
            elif lineToCheckk[0]=="B" and lineToCheckk[1]=="B":
                outFileee.write("0010111\n")
            elif lineToCheckk[0]=="A" and lineToCheckk[1]=="B":
                outFileee.write("0010101\n")
            #numOfIns+=1
        elif Checker[0]==2 and Checker[1]==1 and Checker[2]==1 and Checker[3]==0:
            if lineToCheckk[1]=="A" and lineToCheckk[0] in litListt:
                outFileee.write("0111100 ")
                printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
            elif lineToCheckk[1]=="B" and lineToCheckk[0] in litListt:
                outFileee.write("0111101 ")
                printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
        elif Checker[0]==1 and Checker[1]==1 and Checker[2]==1 and Checker[3]==0:
            if lineToCheckk[0]=="B":
                outFileee.write("0111110\n")
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="XOR":
        lineToCheckk=deleteStuff(currLinea[1])[0]
        #print(lineToCheckk)
        if Checker[0]==2 and Checker[1]==0:
            if lineToCheckk[0]=="A" and lineToCheckk[1]=="B":
                outFileee.write("0011000\n")
            elif lineToCheckk[0]=="B" and lineToCheckk[1]=="A":
                outFileee.write("0011001\n")
            elif lineToCheckk[0]=="A" and lineToCheckk[1] in litListt:
                outFileee.write("0011010 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,2,varDataLocDictt,outFileee)
            elif lineToCheckk[0]=="B" and lineToCheckk[1] in litListt:
                outFileee.write("0011011 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,2,varDataLocDictt,outFileee)
            #numOfIns+=1
        elif Checker[0]==2 and Checker[1]==1 and Checker[2]==0 and Checker[3]==0:
            if lineToCheckk[0]=="A" and lineToCheckk[1] in litListt:
                outFileee.write("0111111 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
            elif lineToCheckk[0]=="B" and lineToCheckk[1] in litListt:
                outFileee.write("1000000 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
            elif lineToCheckk[0]=="A" and lineToCheckk[1]=="B":
                outFileee.write("1000001\n")
        elif Checker[0]==1 and Checker[1]==1 and Checker[2]==1 and Checker[3]==0:
            if lineToCheckk[0] in litListt:
                outFileee.write("1000010 ")
                printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="SHL":
        lineToCheckk=deleteStuff(currLinea[1])[0]
        #print(lineToCheckk)
        if Checker[0]==2 and Checker[1]==0:
            if lineToCheckk[0]=="A" and lineToCheckk[1]=="A":
                outFileee.write("0011100\n")
            elif lineToCheckk[0]=="B" and lineToCheckk[1]=="A":
                outFileee.write("0011110\n")
            elif lineToCheckk[0]=="B" and lineToCheckk[1]=="B":
                outFileee.write("0011111\n")
            elif lineToCheckk[0]=="A" and lineToCheckk[1]=="B":
                outFileee.write("0011101\n")
            #numOfIns+=1
        elif Checker[0]==2 and Checker[1]==1 and Checker[2]==1 and Checker[3]==0:
            if lineToCheckk[1]=="A" and lineToCheckk[0] in litListt:
                outFileee.write("1000011 ")
                printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
            elif lineToCheckk[1]=="B" and lineToCheckk[0] in litListt:
                outFileee.write("1000100 ")
                printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
        elif Checker[0]==1 and Checker[1]==1 and Checker[2]==1 and Checker[3]==0:
            if lineToCheckk[0]=="B":
                outFileee.write("1000101\n")

        else:
            failLista.append([currLinea ,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="SHR":
        lineToCheckk=deleteStuff(currLinea[1])[0]
        #print(lineToCheckk)
        if Checker[0]==2 and Checker[1]==0:
            if lineToCheckk[0]=="A" and lineToCheckk[1]=="A":
                outFileee.write("0100000\n")
            elif lineToCheckk[0]=="B" and lineToCheckk[1]=="A":
                outFileee.write("0100010\n")
            elif lineToCheckk[0]=="B" and lineToCheckk[1]=="B":
                outFileee.write("0100011\n")
            elif lineToCheckk[0]=="A" and lineToCheckk[1]=="B":
                outFileee.write("0100001\n")
            #numOfIns+=1
        elif Checker[0]==2 and Checker[1]==1 and Checker[2]==1 and Checker[3]==0:
            if lineToCheckk[1]=="A" and lineToCheckk[0] in litListt:
                outFileee.write("1000110 ")
                printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
            elif lineToCheckk[1]=="B" and lineToCheckk[0] in litListt:
                outFileee.write("1000111 ")
                printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
        elif Checker[0]==1 and Checker[1]==1 and Checker[2]==1 and Checker[3]==0:
            if lineToCheckk[0]=="B":
                outFileee.write("1001000\n")
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="INC":
        lineToCheckk=deleteStuff(currLinea[1])[0]
        if Checker[0]==1 and Checker[1]==0:
            if lineToCheckk[0]=="B":
                outFileee.write("0100100\n")
            #numOfIns+=1
        elif Checker[0]==1 and Checker[1]==1 and Checker[2]==1:
            if lineToCheckk[0]=="B":
                outFileee.write("1001010\n")
            elif lineToCheckk[0] in litListt:
                outFileee.write("1001001 ")
                printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="RST":
        lineToCheckk=deleteStuff(currLinea[1])[0]
        if Checker[0]==1 and Checker[1]==1 and Checker[2]==1:
            if lineToCheckk[0]=="B":
                outFileee.write("1001100\n")
            elif lineToCheckk[0] in litListt:
                outFileee.write("1001011 ")
                printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="CMP":
        lineToCheckk=deleteStuff(currLinea[1])[0]
        if Checker[0]==2 and Checker[1]==0:
            if lineToCheckk[0]=="A" and lineToCheckk[1]=="B":
                outFileee.write("1001101\n")
            elif lineToCheckk[0]=="A" and lineToCheckk[1] in litListt:
                outFileee.write("1001110 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,2,varDataLocDictt,outFileee)
            elif lineToCheckk[0]=="B" and lineToCheckk[1] in litListt:
                outFileee.write("1001111 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,2,varDataLocDictt,outFileee)
            #numOfIns+=1
        elif Checker[0]==2 and Checker[1]==1 and Checker[2]==0 and Checker[3]==0:
            if lineToCheckk[0]=="A" and lineToCheckk[1] in litListt:
                outFileee.write("1010000 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
            elif lineToCheckk[0]=="B" and lineToCheckk[1] in litListt:
                outFileee.write("1010001 ")
                printStuffToFile(lineToCheckk[1],varDictt,varDataDictt,litDictt,1,varDataLocDictt,outFileee)
            elif lineToCheckk[0]=="A" and lineToCheckk[1]=="B":
                outFileee.write("1000001\n")
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="JMP":
        lineToCheckk=deleteStuff(currLinea[1])[0]
        #print(Checker)
        if Checker[0]==1 and Checker[1]<=1:
            outFileee.write("1010011 ")
            printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,3,varDataLocDictt,outFileee)
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="JEQ":
        lineToCheckk=deleteStuff(currLinea[1])[0]
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            outFileee.write("1010100 ")
            printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,3,varDataLocDictt,outFileee)
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="JNE":
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            outFileee.write("1010101 ")
            printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,3,varDataLocDictt,outFileee)
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="JGT":
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            outFileee.write("1010110 ")
            printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,3,varDataLocDictt,outFileee)
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="JLT":
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            outFileee.write("1010111 ")
            printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,3,varDataLocDictt,outFileee)
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="JGE":
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            outFileee.write("1011000 ")
            printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,3,varDataLocDictt,outFileee)
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="JLE":
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            outFileee.write("1011001 ")
            printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,3,varDataLocDictt,outFileee)
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="JCR":
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            outFileee.write("1011010 ")
            printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,3,varDataLocDictt,outFileee)
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="JOV":
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            outFileee.write("1011011 ")
            printStuffToFile(lineToCheckk[0],varDictt,varDataDictt,litDictt,3,varDataLocDictt,outFileee)
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="CALL":
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            outFileee.write("1010011\n")
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="RET":
        if Checker[0]==0 and Checker[1]<1:
            outFileee.write("1010011\n")
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="POP":
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            outFileee.write("1010011\n")
            #numOfIns+=1
        else:
            failLista.append([currLinea,numOfIns])
            print("Error instruccion n: ",numOfIns)
            print("Datos incorrectos")
            print(currLinea)
            #return nuList
    elif currLinea[0]=="PUSH":
        if 0<=Checker[0]<=1 and Checker[1]<=1:
            outFileee.write("1010011\n")
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
    outFilee=open("salida.out", 'w')
    nuList = []
    propList = []
    varList = []
    litList = []
    litDict = {}
    
    failList = []
    k = 0  #k=0  si se esta probando con CODE:############################################ 
    #print(dataParser(fileList))
    varDict,varDataDict,varDataLocDict = dataParser(fileList)
    #print("asdjasdjask")
    #print(varDict)
    for i in varDict:
        varList.append(i)
        litList.append(i)
    #print(varList)
    #print(fileList[k][0])
    qq = 0
    for currLain in fileList: #Agrega los labels en una lista
        if currLain[0]=="CODE:":
            k=1
            qq=0
            continue
        elif currLain[0][-1]==":" and k==1:
            propList.append(currLain[0])
            #print(currLain[0])
            kk=currLain[0].replace(":","")
            litDict[kk]=qq
        qq+=1    
            #litDict[]
    #print(litDict)
    varList.append("A")
    varList.append("B")
    varList.append("Dir")
    varList.append("0")
    varList.append("1")
    litList.append("1")
    #print("aaaaaa",propList)
    for i in propList:
        i=i.replace(":","")
        varList.append(i)
        litList.append(i)
    #print("bbbbbb",varList)
    #print(varList)
    k = 0  #k=0  si se esta probando con CODE:############################################ 
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
            checc = parserChecker(currLine,numOfIns,varList,failList,outFilee,litList,varDict,litDict,varDataDict,varDataLocDict)
            #print("coomer",parserChecker(currLine,numOfIns,varList,failList))
            if checc:
                failList.append(checc)
            numOfIns+=1
        elif k==1 and currLine[0][-1]==":" and len(currLine)>1:
            lineCheck = currLine.copy()
            #print(lineCheck)
            lineCheck.pop(0)
            #print(lineCheck)
            checc = parserChecker(lineCheck,numOfIns,varList,failList,outFilee,litList,varDict,litDict,varDataDict,varDataLocDict)
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
    dataDataDict = {}
    dataLocList = {}
    defVars= []
    k=-1
    if(fileList[0][0]!="DATA:"):
        #print("error")
        return []
    elif(fileList[0][0]=="DATA:"):
        for currLine in fileList:
            if currLine[0]=="CODE:":
                return dataList,dataDataDict,dataLocList
            elif len(currLine)!=2 and currLine[0]!="DATA:" :
                continue
            elif len(currLine)==2:
                #print("adasdasdlkjasd")
                if currLine[1][0]=="#" :
                    if currLine[1].count("#") == 1:
                        currLine[1] = currLine[1].replace('#','')
                        currLine[1]=int(currLine[1],16)
                        currLine[1] = decimalToBinary(int(currLine[1]))
                        dataList[currLine[0]]=[currLine[1],hex(k)]
                        dataLocList[currLine[0]]=currLine[1]
                        dataDataDict[currLine[0]]=int(k)
                        #print(int(hex(k),16))
                        defVars.append(currLine[0])
                    else:
                        print("Error formato hexadecimal:",currLine[1])
                        
                else:
                    currLine[1] = decimalToBinary(int(currLine[1]))
                    dataList[currLine[0]]=[currLine[1],hex(k)]
                    dataLocList[currLine[0]]=currLine[1]
                    #print("coomer",currLine[1])
                    dataDataDict[currLine[0]]=int((k))
                    #print(int(hex(k),16))
                    defVars.append(currLine[0])
                #print(dataList)
            k+=1
    
    #print(dataList)
    return dataList,dataDataDict,dataLocList



    

fileee = openfile()

#print(fileee)
#print(dataParser(fileee))
#print(dataParser(fileee))
parser(fileee)