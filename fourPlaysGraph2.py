import time

def maxGraphs(numVert, degreePer, givenGames):

    # Bank for all vertices
    verts = []
    for i in range(numVert):
        verts.append(i)

    # List of edges
    adjList = []
    for i in verts:
        adjList.append([])

    for i in givenGames:
        adjList[i[0]].append(i[1])
        adjList[i[1]].append(i[0])
    
    for i in verts:
        if len(adjList[i]) == degreePer:
            verts.remove(i)
        if len(adjList[i]) > degreePer:
            return -1

    # Total graphs
    res = 0

    # Current vertice
    cur = 0

    res = findMaxGraphs(numVert, degreePer, verts, adjList, cur, res)

    return res

def findMaxGraphs(numVert, degreePer, verts, adjList, cur, res):

    # Find how many edges in current graph
    currentSize = 0
    for i in adjList:
        currentSize += len(i)

    # Check if we have a complete graph
    if currentSize < numVert*degreePer:
        for v in verts:
            if v != cur and not adjList[v].count(cur):
                copyList = []
                for i in adjList:
                    copyList.append(i.copy())
                copyList[v].append(cur)
                copyList[cur].append(v)
                copyVerts = verts.copy()
                if len(copyList[v]) == degreePer:
                    copyVerts.remove(v)
                if len(copyList[cur]) == degreePer:
                    copyVerts.remove(cur)

                if len(copyVerts) > 0:
                    res = findMaxGraphs(numVert, degreePer,copyVerts, copyList, copyVerts[0], res)
                else:
                    res = findMaxGraphs(numVert, degreePer,copyVerts, copyList, -1, res)
    
    else:
        #print(adjList)
        res += 1
    
    return res

# Driver Code
if __name__=="__main__":
    startTime = time.time()
    numVert = 6
    degreePer = 3
    #givenGames = [[0, 3], [0, 4], [1, 5]]
    givenGames = []
    print(maxGraphs(numVert, degreePer, givenGames))
    print("--- %s second ---" % (time.time() - startTime))