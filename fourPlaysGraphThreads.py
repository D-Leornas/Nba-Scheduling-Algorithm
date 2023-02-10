import threading
from threading import Thread
import time
class CustomThread(Thread):
    def __init__(self, numVert, degreePer, verts, adjList, noPlays, cur):

        Thread.__init__(self)
        

        # Current vertice

        self.numVert = numVert
        self.degreePer = degreePer
        self.noPlays = noPlays
        self.verts = verts
        self.adjList = adjList
        self.cur = cur
        self.value = 0

    def run(self):

        # Find how many edges in current graph
        currentSize = 0
        for i in self.adjList:
            currentSize += len(i)

        # Check if we have a complete graph
        if currentSize < self.numVert*self.degreePer:
            for v in self.verts:
                if v != self.cur and not self.adjList[v].count(self.cur) and not self.noPlays[self.cur].count(v) and not self.noPlays[v].count(self.cur):
                    copyList = []
                    for i in self.adjList:
                        copyList.append(i.copy())
                    copyList[v].append(self.cur)
                    copyList[self.cur].append(v)
                    copyVerts = self.verts.copy()
                    if len(copyList[v]) == self.degreePer:
                        copyVerts.remove(v)
                    if len(copyList[self.cur]) == self.degreePer:
                        copyVerts.remove(self.cur)

                    if len(copyVerts) > 0:
                        t = CustomThread(self.numVert, self.degreePer, copyVerts, copyList, self.noPlays, copyVerts[0])
                        t.start()
                    else:
                        t = CustomThread(self.numVert, self.degreePer, copyVerts, copyList, self.noPlays, -1)
                        t.start()
                    t.join()
                    data = t.value
                    self.value += data
        else:
            #print(adjList)
            self.value += 1

# Driver Code
if __name__=="__main__":
    startTime = time.time()
    numVert = 10
    degreePer = 2
    #givenGames = [[0, 3], [0, 4], [1, 5]]
    givenGames = []
    noPlays = []
    for i in range(numVert):
        noPlays.append([])

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

    thread = CustomThread(numVert, degreePer, verts, adjList, noPlays, 0)
    
    thread.start()

    thread.join()

    data = thread.value
    print(data)
    #print(maxGraphs(numVert, degreePer, givenGames, noPlays))
    print("--- %s second ---" % (time.time() - startTime))
    