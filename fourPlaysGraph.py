import math
import itertools
# Python 3 implementation of the approach
 
# Function to return the value of
# Binomial Coefficient C(n, k)
# n is number of ways to choose between two vertices, k is the number of edges in the graph
# v is number of vertices, d is max degree
def maxGraphs(k, v, d):
    adj = []
    for i in range(v):
        adj.append([])
    res = 0
    bank = []

    res = findMaxGraphs(k, v, d, res, adj, 0, bank)
 
    return res
 
# res is result, s is keeping track of degrees as to not reach maximum, c is current vertice
def findMaxGraphs(k, v, d, res, adj, c, bank):
    if nestedSum(adj) < k:
        # This range needs to be starting from the first element in adj[c]
        for i in range(v):
            if len(adj[i]) < d and len(adj[c]) < d and i != c and not adj[i].count(c):
                tempAdj = []
                for j in adj:
                    tempAdj.append(j.copy())
                tempAdj[i].append(c)
                tempAdj[c].append(i)
                #adj[i].append(c)
                #adj[c].append(i)

                
                res = findMaxGraphs(k, v, d, res, tempAdj, i, bank)

    else:
        totalEdges = 0
        for i in adj:
            totalEdges += len(i)
        if totalEdges == k and checkIsomorphism(adj, bank, v):
        #if totalEdges == k:
            bank.append([])
            res +=  1
            tempAdj = []
            for i in adj:
                bank[len(bank)-1].append(i.copy())
            print(adj)
    return res
 
def checkIsomorphism(adj, bank, n):
    numSame = 0
    for i in bank:
        for (j, k) in zip(adj, i):
            for perm in itertools.permutations(j):
                if list(perm) == k:
                    numSame += 1
                    break
        if numSame == n:
            return False
    return True

def nestedSum(L):
    total = 0  # don't use `sum` as a variable name
    for i in L:
        for j in i:
            total += 1
    return total

# Driver Code
if __name__=="__main__":
     
    # N vertices, M edges, D degree per edge
    # 15 Vertices for 15 teams
    # 45 edges because 15 teams face 6 opposing teams (15*6) and divide that by 2 since the graph is undirected
    N = 4
    D = 2
    M = N*D
 
    # P = 105 way to choose 2 vertices
    #P = (N * (N - 1)) // 2
    print(maxGraphs(M, N, D))