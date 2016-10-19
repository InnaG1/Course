import json

def hammingDistance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))

class Cluster:
    def __init__(self,leader):
        self.Leader = leader
        self.Visited = False
def getLeader(vartices, v):
    current = v
    i =0
    while vartices[current].Leader!=current:
        current = vartices[current].Leader
        i=i+1
    return current,i
def UnionFind(vartices,v,w):
        sameCluster = True
        vLeader,vdeep = getLeader(vartices,v)
        wLeader,wdeep = getLeader(vartices,w)
        if vLeader!=wLeader:
            if wdeep>vdeep:
                t= vLeader
                vLeader = wLeader
                wLeader = t
            vartices[wLeader].Leader = vLeader
            sameCluster =False
        return sameCluster
            


with open("Algo2_Week2_Clustering_BIG_Data.txt","r") as file:
    t,n = map(int,file.next().split())
    
    vertices ={}
    for line in file:
        splitted = line.strip()
        vertices[splitted] = Cluster(splitted)
    numClusters = len(vertices)
    currentCount = 0
    for key, value in vertices.iteritems():
        currentCount+=1
        if currentCount%1000==0:
            print(currentCount,numClusters,currentCount/numClusters)
        sp = list(map(int,key.split()))
        value.Visited= True;
        for i in range(n):
            for j in range(i,n):
                if i==j:
                    sp[i]=abs(sp[i]-1)
                else:
                    sp[i]=abs(sp[i]-1)
                    sp[j]=abs(sp[j]-1)
                joined = ' '.join(map(str, sp))
                if joined in vertices.keys() and vertices[joined].Visited ==False:
                    sameCluster =UnionFind(vertices,joined,key)
                    if sameCluster==False:
                        numClusters-=1
                #rollback
                if i==j:
                    sp[i]=abs(sp[i]-1)
                else:
                    sp[i]=abs(sp[i]-1)
                    sp[j]=abs(sp[j]-1)

    print(numClusters)
                                        
                

