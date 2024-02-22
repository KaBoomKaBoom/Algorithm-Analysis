class Algorithms:

    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1

    def quick_sort(array, low, high):
        if low < high:
            pi = partition(array, low, high)
            quicksort(array, low, pi - 1)
            quicksort(array, pi + 1, high)
    
    def heapify(arr, N, i):
        largest = i 
        l = 2 * i + 1
        r = 2 * i + 2    
    
        if l < N and arr[largest] < arr[l]:
            largest = l
    
        if r < N and arr[largest] < arr[r]:
            largest = r
    
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i] 
    
            heapify(arr, N, largest)

    def heap_sort(arr):
        N = len(arr)
 
        for i in range(N//2 - 1, -1, -1):
            heapify(arr, N, i)
    
        for i in range(N-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i] 
            heapify(arr, i, 0)

    def mergeSort(arr):
        if len(arr) > 1:
            mid = len(arr)//2

            L = arr[:mid]
    
            R = arr[mid:]
    
            mergeSort(L)
    
            mergeSort(R)
    
            i = j = k = 0
    
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
    
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
    
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1