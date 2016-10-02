import json
  
m =1000000007
def validateInput(inputString):
    valid = True
    if len(inputString)<=2:
        return False
    if inputString[0] =="*" or inputString[len(inputString)-1]=="*":
        return False
    for i in range(1,len(inputString)-1):
        if (inputString[i-1] == "*" and inputString[i]=="*" and inputString[i+1]=="*"):
            return False
    return True
def calculateMod(b,e,m):
    c = 1
    ee= 0
    while(ee<e):
        ee+=1
        c = (b*c) % m
    return m3

def getNumberString(j, inputString):
    numberString = ""
    while j<len(inputString) and inputString[j].isdigit():
          numberString = numberString+inputString[j] 
          j+=1
    return numberString

def calculate(inputString):
    if validateInput(inputString)==False:
        print("Syntax Error")
        return
    stack = []
    i = 0
    while i<len(inputString)-1:
        if inputString[i].isdigit():
            s = getNumberString(i,inputString)
            stack.append(int(s))
            i+=len(s)
        elif inputString[i]=="*" and inputString[i+1]=="*":
            a = stack.pop()
            s = getNumberString(i+2,inputString)
            stack.append(pow(a,int(s),m))
            i+=(2+len(s))
        else:
            s = getNumberString(i+1,inputString)
            stack.append(int(s))
            i+=(1+len(s))
    mul = 1
    for i in range(0, len(stack)):
        mul = mul*stack[i]%m 
    print(mul%m)

# print(validateInput("5***5"))
calculate("669705920769**417307587847*95592825192**429*30*6240385314046**4875557899888791*18689733631**7973652903985**8231102*1151550*3343359624166743*40288819**658**77798760756060872*50104084287613**9304303376122839**582480288999190*586724*895458*6545370775*29314710**9114344620822212**937763539**6664791667124*1**68772596150*655*79955264380*8882**95569094076**562221*720460340232876*11995530451728**35928024477834923*1250939782640341**65027445*60488**24*703763**6752218*239690013172**90181826273967**418133683*2387737*70736393828603*85762*2**603**402764**95942*533077218175031**19956*8*240769588652*852089804430**3**793613**36894667**12965130911307**923050*4754509075288*1779164**1570490**44609910187127153*16216891720760*832452988930**2**4*7916774937150**33755179*94664*91288026584052**1373*6795282892840519*111324212818374**71488123406705*6112530*6933341*96*8311880941068898**667**9274040201**540603656637**5480166370117**808**58726**36120967915630**1127**7803*496347*494*4869918**5812043617167446")

# print(calculateMod(669705920769,417307587847,1000000007))    
# print(pow(669705920769,417307587847,1000000007))    

# tests = int(input())
# for i in range(0, tests):
#     calculate(input())