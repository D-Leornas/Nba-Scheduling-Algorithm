import threading
from threading import Thread
from threading import Lock
import time


class CustomThread(Thread):
    def __init__(   self, numVert, degreePer, verts, adjList, noPlays, cur, maxDepth, depth, thisLock, total):

        Thread.__init__(self)

        # Current vertice

        self.numVert = numVert
        self.degreePer = degreePer
        self.noPlays = noPlays
        self.verts = verts
        self.adjList = adjList
        self.cur = cur
        self.maxDepth = maxDepth
        self.depth = depth
        self.thisLock = thisLock
        self.total = total

    def run(self):
        # Find how many edges in current graph
        currentSize = 0
        for i in self.adjList:
            currentSize += len(i)

        threadTracker = []
        threadCounter = 0

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

                    if self.depth <= self.maxDepth:
                        newLock = Lock()
                        newTotal = 0
                        if len(copyVerts) > 0:
                            #print("Creating Thread")
                            threadTracker.append(CustomThread(self.numVert, self.degreePer, copyVerts, copyList, self.noPlays, copyVerts[0], self.maxDepth, self.depth + 1, newLock, newTotal))
                            threadTracker[threadCounter].start()
                            threadCounter += 1
                            #t = CustomThread(self.numVert, self.degreePer, copyVerts, copyList, self.noPlays, copyVerts[0])
                            #t.start()
                            #t.join()

                        else:
                            #print("Creating Thread")
                            threadTracker.append(CustomThread(self.numVert, self.degreePer, copyVerts, copyList, self.noPlays, -1, self.maxDepth, self.depth + 1))
                            threadTracker[threadCounter].start()
                            threadCounter += 1
                            #t = CustomThread(self.numVert, self.degreePer, copyVerts, copyList, self.noPlays, -1)
                            #t.start()
                    else:
                        if len(copyVerts) > 0:
                            self.total += findMaxGraphs(numVert, degreePer, copyVerts, copyList, noPlays, copyVerts[0], 0)
                        else:
                            self.total += findMaxGraphs(numVert, degreePer, copyVerts, copyList, noPlays, -1, 0)

#            total = 0
            for i in range(0, threadCounter):
                #print("Joining thread")
                threadTracker[i].join()
                self.total += threadTracker[i].total
#                total += threadTracker[i].value
#            
#            self.value += total
            
        else:
            #print(adjList)
            #print("Thread completed perm")
            with thisLock:
                #print("Thread got thisLock")
                self.total += 1

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

    maxDepth = 2

    thisLock = Lock()
    total = 0

    thread = CustomThread(numVert, degreePer, verts, adjList, noPlays, 0, maxDepth, 0, thisLock, total)
    
    thread.start()

    thread.join()

    #data = thread.value
    #print(data)
    print(thread.total)
    #print(maxGraphs(numVert, degreePer, givenGames, noPlays))
    print("--- %s second ---" % (time.time() - startTime))
    