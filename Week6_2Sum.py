import json 

def main ():
    
    dictionary = {}

    with open("Week6_2Sum_Data.txt","r") as file:
        for line in file:
            dictionary[int(line)] = True
    count =0
    for t in range(-10000,10001):
        for x in dictionary.keys():
            if t-x in dictionary and t-x !=x:
                count+=1
    print(count)
                
        


main()
