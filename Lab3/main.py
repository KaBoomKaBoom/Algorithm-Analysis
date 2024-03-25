import time
import matplotlib.pyplot as plt
from Algorithms import Graph
import pandas as pd

graph1 = Graph()
graph1.addEdge(1, 2)
graph1.addEdge(1, 3)
graph1.addEdge(2, 4)
graph1.addEdge(3, 4)

graph2 = Graph()
graph2.addEdge(1, 2)
graph2.addEdge(1, 3)
graph2.addEdge(2, 4)
graph2.addEdge(2, 5)
graph2.addEdge(3, 5)
graph2.addEdge(4, 5)

graph3 = Graph()
graph3.addEdge(1, 2)
graph3.addEdge(1, 3)
graph3.addEdge(2, 4)
graph3.addEdge(2, 5)
graph3.addEdge(3, 5)
graph3.addEdge(4, 6)
graph3.addEdge(5, 6)

graph4 = Graph()
graph4.addEdge(1, 2)
graph4.addEdge(1, 3)
graph4.addEdge(2, 4)
graph4.addEdge(2, 5)
graph4.addEdge(3, 5)
graph4.addEdge(4, 6)
graph4.addEdge(5, 6)
graph4.addEdge(3, 6)

graph5 = Graph()
graph5.addEdge(1, 2)
graph5.addEdge(1, 3)
graph5.addEdge(2, 4)
graph5.addEdge(2, 5)
graph5.addEdge(3, 5)
graph5.addEdge(4, 6)
graph5.addEdge(5, 6)
graph5.addEdge(6, 7)

graphs=[graph1, graph2, graph3, graph4, graph5]
timeDFS = []
timeBFS = []
for i in range(5):
    start = time.perf_counter()
    graphs[i].DFS(1)
    end = time.perf_counter()
    timeDFS.append(end - start)

print(timeDFS)
plt.plot([1,2,3,4,5], timeDFS ,label="DFS")
plt.xlabel('test')
plt.ylabel('Time')
plt.title('Execution Time')
plt.legend()
plt.show()
