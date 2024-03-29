from collections import defaultdict
from collections import defaultdict, deque
 
# This class represents a directed graph using
# adjacency list representation
class GraphDFS:
 
    # Constructor
    def __init__(self):
 
        # Default dictionary to store graph
        self.graph = defaultdict(list)
 
     
    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
     
    # A function used by DFS
    def DFSUtil(self, v, visited):
 
        # Mark the current node as visited
        # and print it
        visited.add(v)
        #print(v, end=' ')
 
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
 
     
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):
 
        # Create a set to store visited vertices
        visited = set()
 
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)
 
class GraphBFS:
    def __init__(self):
        self.adjList = defaultdict(list)
 
    # Function to add an edge to the graph
    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u) # If the graph is undirected, add this line
 
    def show(self, adjList):
        for key, value in adjList.items(): # Change adjList to self.adjList
            print(key, "   ", value,"\n")
 
    # Function to perform Breadth First Search on a graph represented using adjacency list
    def bfs(self, startNode):
        # Create a queue for BFS
        queue = deque()
        max_node = max(self.adjList.keys(), default=-1) # Get the maximum node value
        visited = [False] * (max_node + 1) # Initialize the visited list
 
        # Mark the current node as visited and enqueue it
        visited[startNode] = True
        queue.append(startNode)
 
        # Iterate over the queue
        while queue:
            # Dequeue a vertex from queue and print it
            currentNode = queue.popleft()
            #print(currentNode, end=" ")
 
            # Get all adjacent vertices of the dequeued vertex currentNode
            # If an adjacent has not been visited, then mark it visited and enqueue it
            for neighbor in self.adjList[currentNode]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)