import time
import matplotlib.pyplot as plt
import Algorithms as Algorithms
import sys
from tabulate import tabulate

sys.setrecursionlimit(1000000)
alg = Algorithms.Algorithms()
firstInput = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
secondInput = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

# Test the time of execution of the recursive approach
timeRecursive = []
for n in firstInput:
    start = time.perf_counter()
    alg.recursiveAproach(n)
    end = time.perf_counter()
    timeRecursive.append(end - start)
plt.plot(firstInput, timeRecursive, label="Recursive")
plt.xlabel('Input Size')
plt.ylabel('Time')
plt.title('Execution Time')
plt.legend()
plt.show()


# Test the time of execution of the iterative approach
timeIterative = []
for n in firstInput:
    start = time.perf_counter()
    alg.iterativeAproach(n)
    end = time.perf_counter()
    timeIterative.append(end - start)
plt.plot(firstInput, timeIterative, label="Iterative")
plt.xlabel('Input Size')
plt.ylabel('Time')
plt.title('Execution Time')
plt.legend()
plt.show()

# Test the time of execution of the matrix approach
timeMatrix = []
for n in firstInput:
    start = time.perf_counter()
    alg.fibonacci_matrix(n)
    end = time.perf_counter()
    timeMatrix.append(end - start)
plt.plot(firstInput, timeMatrix, label="Matrix")
plt.xlabel('Input Size')
plt.ylabel('Time')
plt.title('Execution Time')
plt.legend()
plt.show()

# Test the time of execution of the memoization approach
timeMemoization = []
for n in firstInput:
    start = time.perf_counter()
    alg.fibonacci_memoization(n)
    end = time.perf_counter()
    timeMemoization.append(end - start)
plt.plot(firstInput, timeMemoization, label="Memoization")
plt.xlabel('Input Size')
plt.ylabel('Time')
plt.title('Execution Time')
plt.legend()
plt.show()

# Test the time of execution of the binet approach
timeBinet = []
for n in firstInput:
    start = time.perf_counter()
    alg.fibonacci_binet(n)
    end = time.perf_counter()
    timeBinet.append(end - start)
plt.plot(firstInput, timeBinet, label="Binet")
plt.xlabel('Input Size')
plt.ylabel('Time')
plt.title('Execution Time')
plt.legend()
plt.show()

# Test the time of execution of the bottom up approach
timeBottomUp = []
for n in firstInput:
    start = time.perf_counter()
    alg.fibonacci_bottom_up(n)
    end = time.perf_counter()
    timeBottomUp.append(end - start)
plt.plot(firstInput, timeBottomUp, label="Bottom Up")
plt.xlabel('Input Size')
plt.ylabel('Time')
plt.title('Execution Time')
plt.legend()
plt.show()

data = []
for i in range(len(firstInput)):
    n = firstInput[i]
    data.append([n, timeRecursive[i],timeIterative[i], timeMatrix[i], timeMemoization[i], timeBinet[i], timeBottomUp[i]])

# Display results in a table
headers = ["Input Size",'Recursive' ,"Iterative", "Matrix", "Memoization", "Binet", "Bottom Up"]
print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

#--------------------------------------------------------------

# Test the time of execution of the iterative approach
timeIterative = []
for n in secondInput:
    start = time.perf_counter()
    alg.iterativeAproach(n)
    end = time.perf_counter()
    timeIterative.append(end - start)
plt.plot(secondInput, timeIterative, label="Iterative")
plt.xlabel('Input Size')
plt.ylabel('Time')
plt.title('Execution Time')
plt.legend()
plt.show()

# Test the time of execution of the matrix approach
timeMatrix = []
for n in secondInput:
    start = time.perf_counter()
    alg.fibonacci_matrix(n)
    end = time.perf_counter()
    timeMatrix.append(end - start)
plt.plot(secondInput, timeMatrix, label="Matrix")
plt.xlabel('Input Size')
plt.ylabel('Time')
plt.title('Execution Time')
plt.legend()
plt.show()

# Test the time of execution of the memoization approach
timeMemoization = []
for n in secondInput:
    start = time.perf_counter()
    alg.fibonacci_memoization(n)
    end = time.perf_counter()
    timeMemoization.append(end - start)
plt.plot(secondInput, timeMemoization, label="Memoization")
plt.xlabel('Input Size')
plt.ylabel('Time')
plt.title('Execution Time')
plt.legend()
plt.show()

# Test the time of execution of the binet approach
timeBinet = []
for n in secondInput:
    start = time.perf_counter()
    alg.fibonacci_binet(n)
    end = time.perf_counter()
    timeBinet.append(end - start)
plt.plot(secondInput, timeBinet, label="Binet")
plt.xlabel('Input Size')
plt.ylabel('Time')
plt.title('Execution Time')
plt.legend()
plt.show()

# Test the time of execution of the bottom up approach
timeBottomUp = []
for n in secondInput:
    start = time.perf_counter()
    alg.fibonacci_bottom_up(n)
    end = time.perf_counter()
    timeBottomUp.append(end - start)
plt.plot(secondInput, timeBottomUp, label="Bottom Up")
plt.xlabel('Input Size')
plt.ylabel('Time')
plt.title('Execution Time')
plt.legend()
plt.show()

data = []
for i in range(len(secondInput)):
    n = secondInput[i]
    data.append([n, timeIterative[i], timeMatrix[i], timeMemoization[i], timeBinet[i], timeBottomUp[i]])

# Display results in a table
headers = ["Input Size", "Iterative", "Matrix", "Memoization", "Binet", "Bottom Up"]
print(tabulate(data, headers=headers, tablefmt="fancy_grid"))



