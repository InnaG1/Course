import json

def main():
    left = [] # will contain all elements with - as this arr should give use Max and we have only min 
    right = [] # will contain rest of the array after median
    i = 0
    medianCount = 0
    with open ("week6_median.txt", "r") as file:
        for line in file:
            number = int(line)
            # spesial cases for 0 and 1 
            if len(left) ==0:
                insertMin(-1*number,left)
            elif len(right)==0:
                    if (number < -1*left[0]):
                        insertMin(-1*left[0],right)
                        popMin(left)
                        insertMin(-1*number,left)
                    else:
                        insertMin(number,right)
            else:        
                if i%2==0:
                #add to the left 
                    if(number>right[0]):
                        insertMin(-1*right[0],left)
                        popMin(right)
                        insertMin(number, right)
                    else:
                        insertMin(-1*number, left)
                else: 
                   if number < -1* left[0]:
                       insertMin(-1*left[0],right)
                       popMin(left)
                       insertMin(-1*number,left)
                   else:
                        insertMin(number, right)    
            medianItself = -1*left[0]
            medianCount+=-1*left[0]
            i+=1
    print(medianCount%10000)      
def swap(a,b,arr):
    t = arr[a]
    arr[a] = arr[b]
    arr[b] = t

def insertMin(a,arr):
    arr.append(a)
    lastInd = len(arr)-1
    parent = int((lastInd+1)/2) -1
    while parent>=0 and arr[lastInd]<arr[parent]:
        swap(parent, lastInd, arr)
        lastInd = parent
        parent = int((lastInd+1)/2) -1

def popMin(arr):
    if len(arr) > 1:
        lastEl = arr.pop()
        arr[0] = lastEl
        lastIndInarr = len(arr)-1
        parent =0
        childLeft = 2*parent +1
        childRight = 2* parent +2
        while ( childLeft <=lastIndInarr and ( arr[childLeft] < arr[parent] or (childRight<=lastIndInarr and arr[childRight] < arr[parent]) )  ):
            if(childRight>lastIndInarr):
                childRight = childLeft

            if ( arr[childLeft] <= arr[childRight] ):
                swap(childLeft, parent, arr)
                parent = childLeft
            else:
                swap(childRight, parent,arr)
                parent = childRight
            childLeft = 2*parent +1
            childRight = 2* parent +2
    else: 
        last = arr.pop()
        if len(arr)>0:
            arr[0] = last

        



if __name__ == '__main__':
    main()
    