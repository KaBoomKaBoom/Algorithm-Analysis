class Algorithms:

    def partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1

    def quicksort(self, array, low, high):
        if low < high:
            pi = Algorithms.partition(self, array, low, high)
            Algorithms.quicksort(self, array, low, pi - 1)
            Algorithms.quicksort(self, array, pi + 1, high)
    
    def heapify(self, arr, N, i):
        largest = i 
        l = 2 * i + 1
        r = 2 * i + 2    
    
        if l < N and arr[largest] < arr[l]:
            largest = l
    
        if r < N and arr[largest] < arr[r]:
            largest = r
    
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i] 
    
            Algorithms.heapify(self, arr, N, largest)

    def heap_sort(self, arr):
        N = len(arr)
 
        for i in range(N//2 - 1, -1, -1):
            Algorithms.heapify(self, arr, N, i)
    
        for i in range(N-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i] 
            Algorithms.heapify(self, arr, i, 0)

    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2

            L = arr[:mid]
    
            R = arr[mid:]
    
            Algorithms.mergeSort(self, L)
    
            Algorithms.mergeSort(self, R)
    
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

    def count_sort(self, input_array):

        M = max(input_array)
        count_array = [0] * (M + 1)
    
        # Mapping each element of input_array as an index of count_array
        for num in input_array:
            count_array[num] += 1
    
        # Calculating prefix sum at every index of count_array
        for i in range(1, M + 1):
            count_array[i] += count_array[i - 1]
    
        # Creating output_array from count_array
        output_array = [0] * len(input_array)
    
        for i in range(len(input_array) - 1, -1, -1):
            output_array[count_array[input_array[i]] - 1] = input_array[i]
            count_array[input_array[i]] -= 1
    
        return output_array