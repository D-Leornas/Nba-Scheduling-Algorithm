import java.util.*;
import java.util.concurrent.*;
public class fourPlaysGraphThreadsJava2 {
    public static void main(String[] args) {
        long startTime = System.nanoTime();
        int numVert = 4;
        int degreePer = 2;
        //givenGames = [[0, 3], [0, 4], [1, 5]]
        //ArrayList<ArrayList<Integer>> givenGames = new ArrayList<ArrayList<Integer>>();
        ArrayList<ArrayList<Integer>> noPlays = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i < numVert; i++) {
            noPlays.add(new ArrayList<Integer>());
        }

        ArrayList<Integer> verts = new ArrayList<Integer>();
        for (int i = 0; i < numVert; i++) {
            verts.add(i);
        }

        // List of edges
        ArrayList<ArrayList<Integer>> adjList = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i < numVert; i++) {
            adjList.add(new ArrayList<Integer>());
        }
        
        for (int i = 0; i < verts.size(); i++) {
            if (adjList.get(i).size() == degreePer) {
                verts.remove(i);
            }
        }

        int maxDepth = 0;

        Semaphore mutex = new Semaphore(1);
        int total = 0;

        CustomThread thread = new CustomThread(numVert, degreePer, verts, adjList, noPlays, 0, maxDepth, 0, mutex, total);
        
        thread.start();

        //while (thread.isAlive()) {
        //    System.out.println(Thread.activeCount());
        //}

        try {
            thread.join();
        }
        catch (InterruptedException e) {
            System.out.println(e);
        }

        int data = thread.total;
        System.out.println(data);
        //print(thread.total);
        //print(maxGraphs(numVert, degreePer, givenGames, noPlays))
        System.out.printf("--- %f seconds ---", (System.nanoTime() - startTime)/1000000000f);
    }
}

class CustomThread extends Thread {
    int numVert;
    int degreePer;
    ArrayList<ArrayList<Integer>> noPlays;
    ArrayList<Integer> verts;
    ArrayList<ArrayList<Integer>> adjList;
    int cur;
    int maxDepth;
    int depth;
    Semaphore thisLock;
    public int total;

    CustomThread(int numVert, int degreePer, ArrayList<Integer> verts, ArrayList<ArrayList<Integer>> adjList, ArrayList<ArrayList<Integer>> noPlays, int cur, int maxDepth, int depth, Semaphore thisLock, int total) {
        this.numVert = numVert;
        this.degreePer = degreePer;
        this.noPlays = new ArrayList<ArrayList<Integer>>(noPlays);
        this.verts = new ArrayList<Integer>(verts);
        this.adjList = new ArrayList<ArrayList<Integer>>(adjList);
        this.cur = cur;
        this.maxDepth = maxDepth;
        this.depth = depth;
        this.thisLock = thisLock;
        this.total = total;
    }

    public void run() {

        ArrayList<CustomThread> threadTracker = new ArrayList<CustomThread>();
        int threadCounter = 0;
        if (depth < maxDepth) {
            for (int i : verts) {
                ArrayList<ArrayList<Integer>> copyList = new ArrayList<ArrayList<Integer>>();
                for(int j = 0; j < adjList.size(); j++) {
                    ArrayList<Integer> temp = new ArrayList<Integer>();
                    for(int k = 0; k < adjList.get(j).size(); k++) {
                        temp.add(adjList.get(j).get(k));
                    }
                    copyList.add(temp);
                }
                ArrayList<Integer> copyVerts = new ArrayList<Integer>(verts);

                Semaphore newLock = new Semaphore(1);
                int newTotal = 0;

                if (copyVerts.size() > 0) {
                    threadTracker.add(new CustomThread(numVert, degreePer, copyVerts, copyList, noPlays, i, maxDepth, depth+1, newLock, newTotal));
                    threadTracker.get(threadCounter).start();
                    threadCounter += 1;
                }
                else {
                    threadTracker.add(new CustomThread(numVert, degreePer, copyVerts, copyList, noPlays, -1, maxDepth, depth+1, newLock, newTotal));
                    threadTracker.get(threadCounter).start();
                    threadCounter += 1;
                }
            }
        }
        else {
            ArrayList<ArrayList<Integer>> copyList = new ArrayList<ArrayList<Integer>>();
            for(int j = 0; j < adjList.size(); j++) {
                ArrayList<Integer> temp = new ArrayList<Integer>();
                for(int k = 0; k < adjList.get(j).size(); k++) {
                    temp.add(adjList.get(j).get(k));
                }
                copyList.add(temp);
            }
            ArrayList<Integer> copyVerts = new ArrayList<Integer>(verts);

            if (copyVerts.size() > 0) {
                this.total += findMaxGraphs(numVert, degreePer, copyVerts, copyList, noPlays, copyVerts.get(0), 0);
            }
            else {
                this.total += findMaxGraphs(numVert, degreePer, copyVerts, copyList, noPlays, -1, 0);
            }
        }

        for (int i = 0; i < threadCounter; i++) {
            try {
                threadTracker.get(i).join();
            }
            catch (InterruptedException e) {
                System.out.println(e);
            }
            this.total += threadTracker.get(i).total;
        }
    }

    private int findMaxGraphs(int numVert, int degreePer, ArrayList<Integer> verts, ArrayList<ArrayList<Integer>> adjList, ArrayList<ArrayList<Integer>> noPlays, int cur, int res) {
        int currentSize = 0;
        //System.out.println(adjList);
        for (int i = 0; i < adjList.size(); i++) {
            currentSize += adjList.get(i).size();
        }

        if (currentSize < (numVert*degreePer)) {
            if (cur < numVert/2) {
                for (int i : verts) {
                    if (i > cur && adjList.get(cur).size() < degreePer &&  adjList.get(i).size() < degreePer && !(adjList.get(i).contains(cur)) && !(noPlays.get(i).contains(cur))) {
                        ArrayList<ArrayList<Integer>> copyList = new ArrayList<ArrayList<Integer>>();
                        for(int j = 0; j < adjList.size(); j++) {
                            ArrayList<Integer> temp = new ArrayList<Integer>();
                            for(int k = 0; k < adjList.get(j).size(); k++) {
                                temp.add(adjList.get(j).get(k));
                            }
                            copyList.add(temp);
                        }
                        copyList.get(i).add(cur);
                        copyList.get(cur).add(i);
                        ArrayList<Integer> copyVerts = new ArrayList<Integer>(verts);
                        if (copyList.get(i).size() == degreePer)
                            copyVerts.remove(verts.indexOf(i));
                        if (copyList.get(cur).size() == degreePer)
                            copyVerts.remove(verts.indexOf(cur));

                        if (copyVerts.size() > 0) {
                            res = findMaxGraphs(numVert, degreePer, copyVerts, copyList, noPlays, copyVerts.get(0), res);
                        }
                        else {
                            res = findMaxGraphs(numVert, degreePer, copyVerts, copyList, noPlays, -1, res);
                        }
                    }
                }
            }
            else {
                for (int i : verts) {
                    if (i > cur && adjList.get(cur).size() < degreePer &&  adjList.get(i).size() < degreePer && !(adjList.get(i).contains(cur)) && !(noPlays.get(i).contains(cur))) {
                        ArrayList<ArrayList<Integer>> copyList = new ArrayList<ArrayList<Integer>>();
                        for(int j = 0; j < adjList.size(); j++) {
                            ArrayList<Integer> temp = new ArrayList<Integer>();
                            for(int k = 0; k < adjList.get(j).size(); k++) {
                                temp.add(adjList.get(j).get(k));
                            }
                            copyList.add(temp);
                        }
                        copyList.get(i).add(cur);
                        copyList.get(cur).add(i);
                        ArrayList<Integer> copyVerts = new ArrayList<Integer>(verts);
                        if (copyList.get(i).size() == degreePer)
                            copyVerts.remove(verts.indexOf(i));
                        if (copyList.get(cur).size() == degreePer)
                            copyVerts.remove(verts.indexOf(cur));

                        if (copyVerts.size() > 0) {
                            res = findMaxGraphs(numVert, degreePer, copyVerts, copyList, noPlays, copyVerts.get(0), res);
                        }
                        else {
                            res = findMaxGraphs(numVert, degreePer, copyVerts, copyList, noPlays, -1, res);
                        }
                    }
                }
            }
        }
        else {
            System.out.println(adjList);
            res += 1;
        }
        return res;
    }
}