import json



class Cluster:
    def __init__(self,leader,countInCluster):
        self.Leader = leader
        self.Count = countInCluster
def getLeader(vartices, v):
    current = v
    while vartices[current].Leader!=current:
        current = vartices[current].Leader
    return current

def calculate(listOfDistances, t):
    vartices = []
    currectCountOfClusters = t
    #all parents will be clusters
    for i in range(t):
        vert = Cluster(int(i),1)
        vartices.append(vert)
    
    newSorted =sorted(listOfDistances,key = lambda x: x[2])
    iter = 0
    while currectCountOfClusters > 3:
        v= newSorted[iter][0]-1
        w = newSorted[iter][1]-1
        vLeader = getLeader(vartices,v)
        wLeader = getLeader(vartices,w)
        if vLeader==wLeader:
            iter+=1
        else:
            if vartices[vLeader].Count<vartices[wLeader].Count:
                t= vLeader
                vLeader = wLeader
                wLeader = t
            vartices[vLeader].Count+=vartices[wLeader].Count
            vartices[wLeader].Leader = vLeader
            currectCountOfClusters-=1
            if(currectCountOfClusters==4):
                
                print(newSorted[iter],"that was fourth", iter)
            if currectCountOfClusters==3:
                print(newSorted[iter][2],"hmmm",iter)
                print(newSorted[iter-1])
                print(newSorted[iter-2])
                print(newSorted[iter-3])
            iter+=1
    return newSorted[iter]  
    
with open("Algo2_Week2_Clustering_Data.txt","r") as file:
    t = int(file.next())
    
    listOfDistances =[] 
    for line in file:
        splitted = list(map(int,line.split()))
        listOfDistances.append(splitted)
    print(calculate(listOfDistances,t))




        
