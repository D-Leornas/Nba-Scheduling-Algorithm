import time

def maxGraphs(numVert, degreePer, givenGames, noPlays):

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

    res = findMaxGraphs(numVert, degreePer, verts, adjList, noPlays, cur, res)

    return res

def findMaxGraphs(numVert, degreePer, verts, adjList, noPlays, cur, res):

    # Find how many edges in current graph
    currentSize = 0
    for i in adjList: # O(N)
        currentSize += len(i)

    # Check if we have a complete graph
    if currentSize < numVert*degreePer: # O(1)
        for v in verts: # O(N)
            if v != cur and not adjList[v].count(cur) and not noPlays[cur].count(v) and not noPlays[v].count(cur): # O(1)
                copyList = []
                for i in adjList: # O(N)
                    copyList.append(i.copy())
                copyList[v].append(cur)
                copyList[cur].append(v)
                copyVerts = verts.copy()
                if len(copyList[v]) == degreePer:
                    copyVerts.remove(v)
                if len(copyList[cur]) == degreePer:
                    copyVerts.remove(cur)

                # This creates a recursion with depth of N so O(N)
                if len(copyVerts) > 0:
                    res = findMaxGraphs(numVert, degreePer, copyVerts, copyList, noPlays, copyVerts[0], res)
                else:
                    res = findMaxGraphs(numVert, degreePer, copyVerts, copyList, noPlays, -1, res)
    else:
        #print(adjList)
        res += 1
    
    return res

# Driver Code
if __name__=="__main__":
    startTime = time.time()
    numVert = 9 # N
    degreePer = 2
    #givenGames = [[0, 3], [0, 4], [1, 5]]
    givenGames = []
    noPlays = []
    for i in range(numVert): # O(N)
        noPlays.append([])
    print(maxGraphs(numVert, degreePer, givenGames, noPlays))
    print("--- %s second ---" % (time.time() - startTime))