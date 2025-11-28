def is_fibonacci_prime (n):
    #is_fibonacci
    fib = [1, 2]
    if n in fib:
        is_fibonacci = True
        loop_to_be_run = False
    else:
        loop_to_be_run = True
    while loop_to_be_run:
        new = fib[-1]+fib[-2]
        if new == n:
            is_fibonacci = True
            break
        if new>n:
            is_fibonacci = False
            break
        fib.append(new)
    
    #is_prime
    if n<=1:
        return False
    i = 2
    while i < n/2:
        if n%i == 0:
            return False
        i+=1
    
    return is_fibonacci

#testing
for i in [2, 3, 5, 13, 89, 8, 21, 7, 11, 1, 0, 50]:
    print(f"is_fibonacci_prime({i}) =", is_fibonacci_prime(i))

#runtime
n = int(input("Enter number (n): "))
print("Result =", is_fibonacci_prime(n))
import timeit
runtime = timeit.timeit("is_fibonacci_prime(n)", globals=globals(), number = 1000000)
print("Average runtime =", runtime/1000000, "seconds")

#memory usage
import tracemalloc
tracemalloc.start()
is_fibonacci_prime(n)
peak_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("Peak memory usage =", peak_memory, "Bytes")

#steps counting
def orderMod_stepsCounter (a, n):
    steps=1
    if n <= 1:

        steps+=1
        return steps
    
    steps+=1
    if a < n:
        steps+=1

        s = a
        steps+=1
    
    else:
        s = n
        steps+=1

    i = 2
    steps+=1

    steps+=1
    while i<=s:
        steps+=1

        steps+=5
        if a%i == 0 and n%i == 0:

            steps+=1
            return steps
        
        i+=1
        steps+=2

    k = 1
    steps+=1

    while True:

        steps+=3
        if pow(a, k, n) == 1:

            steps+=1
            return steps
        
        k+=1
        steps+=2

print("Number of steps =", orderMod_stepsCounter(10, n))