import json

def main():
    adList = []
    priorityqueueRemoved = {}
    distance =[]
    parent = []

    for i in range(200):
        adList.append([])
        distance.append(1000000)
        parent.append(-1)
        priorityqueueRemoved[i] = 1000000
    with open("dijkstraData.txt","r") as file:
        for line in file:
            splitted = line.split("\t")
            v= int(splitted[0])-1
            weightsList =splitted[1:-1]
            vertexWeightSplitted = [ x.split(",") for x in weightsList]
            vertexWeight = {int(x[0])-1: int(x[1]) for x in vertexWeightSplitted}
            adList[v] = vertexWeight
    distance[0]= 0
    priorityqueueRemoved[0] = 0

    while len(priorityqueueRemoved)>0:
        minval = min(priorityqueueRemoved,key= priorityqueueRemoved.get)
        # indexMin = distance.index(min(distance))
        # indexToDelete = priorityqueueRemoved.index(indexMin)
        for elemkey,elemdist in adList[minval].items():
            Relax(minval,elemkey, elemdist,distance, parent, priorityqueueRemoved)
        priorityqueueRemoved.pop(minval,None)

    print (distance[6],distance[36],distance[58],distance[81],distance[98],distance[114],distance[132],distance[164],distance[187],distance[196])

def Relax(u, v,w, distancearr, parrentarr, priorqrem):
    if distancearr[v]>distancearr[u]+w:
        distancearr[v] = distancearr[u]+w
        priorqrem[v] =distancearr[v] 
        parrentarr[v] = u

main()