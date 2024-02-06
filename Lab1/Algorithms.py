import math


class Algorithms:

    def recursiveAproach(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return Algorithms.recursiveAproach(self, n-1) + Algorithms.recursiveAproach(self, n-2)

    def iterativeAproach(self, n):
        a = 0
        b = 1
        for i in range(n):
            a, b = b, a + b
        return a
    
    def fibonacci_matrix(self, n):
        def matrix_multiply(a, b):
            return [[a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
                    [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]]

        def matrix_power(matrix, n):
            if n == 1:
                return matrix
            elif n % 2 == 0:
                half_power = matrix_power(matrix, n//2)
                return matrix_multiply(half_power, half_power)
            else:
                half_power = matrix_power(matrix, n//2)
                return matrix_multiply(matrix_multiply(half_power, half_power), matrix)

        base_matrix = [[1, 1], [1, 0]]
        result_matrix = matrix_power(base_matrix, n)
        return result_matrix[0][1]

    def fibonacci_memoization(self, n, memo={}):
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = Algorithms.fibonacci_memoization(self, n-1, memo) + Algorithms.fibonacci_memoization(self, n-2, memo)
        return memo[n]


    def fibonacci_binet(self, n):
        sqrt_5 = int(math.sqrt(5))
        phi = (1 + sqrt_5) // 2
        psi = (1 - sqrt_5) // 2
        return int((phi**n - psi**n) // sqrt_5)

    def fibonacci_bottom_up(self, n):
        if n <= 1:
            return n
        fib = [0] * (n + 1)
        fib[1] = 1
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[n]

