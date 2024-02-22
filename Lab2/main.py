import time
import matplotlib.pyplot as plt
import Algorithms as Algorithms
import sys
import pandas as pd
import random

alg = Algorithms.Algorithms()
el = [100, 500, 1000, 5000, 10000,20000,30000,40000, 50000]
arr = [[random.randint(0, 100000) for _ in range(length)] for length in el]
timeQuick = []
for i in arr:
    N = len(i)-1
    start = time.perf_counter()
    alg.quicksort(i,0,N)
    end = time.perf_counter()
    timeQuick.append(end - start)
plt.plot(el, timeQuick, label="Quick Sort")
plt.xlabel('Input Size')
plt.ylabel('Time')
plt.title('Execution Time')
plt.legend()
plt.show()

timeHeap = []
for i in arr:
    start = time.perf_counter()
    alg.heap_sort(i)
    end = time.perf_counter()
    timeHeap.append(end - start)
plt.plot(el, timeHeap, label="Heap Sort")
plt.xlabel('Input Size')
plt.ylabel('Time')
plt.title('Execution Time')
plt.legend()
plt.show()

timeMerge = []
for i in arr:
    start = time.perf_counter()
    alg.mergeSort(i)
    end = time.perf_counter()
    timeMerge.append(end - start)
plt.plot(el, timeMerge, label="Merge Sort")
plt.xlabel('Input Size')
plt.ylabel('Time')
plt.title('Execution Time')
plt.legend()
plt.show()

timeCount = []
for i in arr:
    start = time.perf_counter()
    inter = alg.count_sort(i)
    end = time.perf_counter()
    timeCount.append(end - start)
plt.plot(el, timeCount, label="Count Sort")
plt.xlabel('Input Size')
plt.ylabel('Time')
plt.title('Execution Time')
plt.legend()
plt.show()

# Plotting the data
plt.plot(el, timeQuick, label='QuickSort')
plt.plot(el, timeHeap, label='BubbleSort')
plt.plot(el, timeMerge, label='MergeSort')
plt.plot(el, timeCount, label='CountSort')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithms Comparison')
plt.legend()  # Adding legend
plt.show()

data = []
for i in range(len(el)):
    n = el[i]
    data.append([n, timeQuick[i], timeHeap[i], timeMerge[i], timeCount[i]])

# Display results in a tables
headers = ["Input Size", 'QuickSort', 'HeapSort', 'MergeSort', 'CountSort']
df = pd.DataFrame(data, columns=headers)
print(df)