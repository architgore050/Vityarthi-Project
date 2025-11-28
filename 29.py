def order_mod (a, n):
    #any such k can never be acheaved if n = 1
    if n <= 1:
        return None
    
    #gcd of a and n must be 1
    if a < n:
        s = a
    else: s = n
    i = 2
    while i<=s:
        if a%i == 0 and n%i == 0:
            return None
        i+=1

    #finding k
    k = 1       #k = 0 satisfies the condition every time regardless of a and n if n != 0. but it is only an integer, not a positive integer
    while True:
        if pow(a, k, n) == 1:
            return k
        k+=1

#testing
test_cases = [(1, 7), (2, 7), (2, 9), (4, 9), (2, 4), (6, 15), (2, 11), (3, 11), (10, 17), (7, 19), (4, 17), (3, 13)]
for test_case in test_cases:
    print(f"order_mod{test_case} =", order_mod(test_case[0], test_case[1]))

#runtime
a = int(input("Enter number (a): "))
n = int(input("Enter number (n): "))
print("Result =", order_mod(a, n))
import timeit
runtime = timeit.timeit("order_mod(a, n)", globals=globals(), number = 1000000)
print("Average runtime =", runtime/1000000, "seconds")

#memory usage
import tracemalloc
tracemalloc.start()
order_mod(a, n)
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

print("Number of steps =", orderMod_stepsCounter(a, n))