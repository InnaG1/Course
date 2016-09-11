import json 

def main ():
    
    dictionary = {}
    array = []

    with open("Week6_2Sum_Data.txt","r") as file:
        for line in file:
            dictionary[long(line)] = True
            array.append(long(line))
    array.sort()
    count =0
    for t in range(-10000,10001):
        for x in array:
            if x>t:
                break
            if t-x in dictionary and t-x !=x:
                count+=1
                break

    print(count)
                
        


main()
