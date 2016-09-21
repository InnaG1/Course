import json

def main():
    input = ['* ^ * 0 ',
            '6  | * * ',
            '*  | 5 * ',
            '4  | * 1']
    inputsplitted = []
    for i in range(len(input)):
        t = input[i].split()
        inputsplitted.append(t)
       
    m = len(inputsplitted)
    n = len(inputsplitted[0])
    nn = n-1
    for i in range(0,int(m/2)):
        for j in range(i,nn-i):
            t = inputsplitted[i][j]
            inputsplitted[i][j] = inputsplitted[nn-j][i]
            inputsplitted[nn-j][i] = inputsplitted[nn-i][nn-j]
            inputsplitted[nn-i][nn-j] = inputsplitted[j][nn-i]
            inputsplitted[j][nn-i] = t

    for i in range(n):
       
       print(inputsplitted[i])
    
main()
    