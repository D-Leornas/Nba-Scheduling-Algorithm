import java.util.ArrayList;
import java.util.concurrent.Semaphore;
public class fourPlaysGraphThreadsJava {
    public static void main(String[] args) {
        long startTime = System.nanoTime();
        int numVert = 8;
        int degreePer = 2;
        //givenGames = [[0, 3], [0, 4], [1, 5]]
        ArrayList<ArrayList<Integer>> givenGames = new ArrayList<ArrayList<Integer>>();
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

        int maxDepth = 1;

        Semaphore mutex = new Semaphore(1);
        int total = 0;

        //thread = CustomThread(numVert, degreePer, verts, adjList, noPlays, 0, maxDepth, 0, thisLock, total)
        
        //thread.start()

        //while True:
        //    print(threading.active_count())
        //thread.join()

        //data = thread.value
        //print(data)
        //print(thread.total);
        //print(maxGraphs(numVert, degreePer, givenGames, noPlays))
        System.out.printf("--- %f seconds ---", (System.nanoTime() - startTime)/1000000000f);
    }
}

class CustomThread extends Thread {
    int numVert;
    int degreePer;
    ArrayList<ArrayList<Integer>> noPlays;
    ArrayList<ArrayList<Integer>> verts;
    ArrayList<ArrayList<Integer>> adjList;
    int cur;
    int maxDepth;
    int depth;
    Semaphore thisLock;
    int total;

    CustomThread(int numVert, int degreePer, ArrayList<ArrayList<Integer>> verts, ArrayList<ArrayList<Integer>> adjList, ArrayList<ArrayList<Integer>> noPlays, int cur, int maxDepth, int depth, Semaphore thisLock, int total) {
        this.numVert = numVert;
        this.degreePer = degreePer;
        this.noPlays = noPlays;
        this.verts = verts;
        this.adjList = adjList;
        this.cur = cur;
        this.maxDepth = maxDepth;
        this.depth = depth;
        this.thisLock = thisLock;
        this.total = total;
    }

    public void run() {
        int currentSize = 0;
        for (int i = 0; i < adjList.size(); i++) {
            currentSize += adjList.get(i).size();
        }

        ArrayList<CustomThread> threadTracker;
        int threadCounter = 0;

    }
}